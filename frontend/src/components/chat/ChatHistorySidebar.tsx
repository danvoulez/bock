import React, { useEffect, useState } from "react";
import { supabase } from "../../lib/supabase";

type ChatSession = {
  id: string;
  title: string | null;
  updated_at: string;
};

export function ChatHistorySidebar() {
  const [sessions, setSessions] = useState<ChatSession[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchSessions() {
      setLoading(true);
      const { data } = await supabase
        .from("chat_sessions")
        .select("*")
        .order("updated_at", { ascending: false })
        .limit(30);
      setSessions(data || []);
      setLoading(false);
    }
    fetchSessions();

    // Optional: subscribe to changes
    const sub = supabase
      .channel("chat-sessions")
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "chat_sessions" },
        fetchSessions
      )
      .subscribe();

    return () => {
      supabase.removeChannel(sub);
    };
  }, []);

  return (
    <div>
      <div className="px-6 pb-2 font-semibold text-gray-800 text-sm">Histórico de Chats</div>
      {loading && <div className="px-6 text-xs text-gray-400">Carregando…</div>}
      <ul className="flex flex-col gap-1 px-2">
        {sessions.map((s) => (
          <li
            key={s.id}
            className="px-4 py-2 text-sm rounded hover:bg-orange-100 cursor-pointer truncate"
            title={s.title || s.id}
            // onClick={() => handleSelectSession(s.id)}
          >
            <span className="font-medium">{s.title || `Sessão ${s.id.slice(0, 6)}`}</span>
            <span className="block text-xs text-gray-400">
              {new Date(s.updated_at).toLocaleString("pt-BR")}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}