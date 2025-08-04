import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at: string;
  mcp_payload?: any;
}

export function useChatMessages(sessionId: string) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let subscription: any;
    async function fetchMessages() {
      setLoading(true);
      const { data } = await supabase
        .from("chat_messages")
        .select("*")
        .eq("session_id", sessionId)
        .order("created_at");
      setMessages(data || []);
      setLoading(false);
    }
    fetchMessages();

    subscription = supabase
      .channel("chat-messages")
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "chat_messages" },
        (payload) => {
          fetchMessages();
        }
      )
      .subscribe();

    return () => {
      supabase.removeChannel(subscription);
    };
  }, [sessionId]);

  const sendUserMessage = async (content: string) => {
    const { data } = await supabase
      .from("chat_messages")
      .insert([{ session_id: sessionId, role: "user", content }])
      .select()
      .single();
    setMessages((prev) => [...prev, data]);
  };

  const sendAssistantMessage = async (content: string, mcp_payload?: any) => {
    const { data } = await supabase
      .from("chat_messages")
      .insert([{ session_id: sessionId, role: "assistant", content, mcp_payload }])
      .select()
      .single();
    setMessages((prev) => [...prev, data]);
  };

  return { messages, sendUserMessage, sendAssistantMessage, loading };
}