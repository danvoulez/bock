import { useState, useEffect } from "react";
import { supabase } from "../lib/supabase";

export function useChatSession(selectedSessionId?: string) {
  const [sessionId, setSessionId] = useState(selectedSessionId);

  // On mount: create new session if none selected
  useEffect(() => {
    if (!sessionId) {
      (async () => {
        const { data, error } = await supabase
          .from("chat_sessions")
          .insert({ title: null }) // or add user_id, etc
          .select()
          .single();
        if (data?.id) setSessionId(data.id);
      })();
    }
  }, [sessionId]);

  return { sessionId, setSessionId };
}