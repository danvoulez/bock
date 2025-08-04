import { useRef, useState } from "react";
import { useChatMessages } from "../../hooks/useChatMessages";
import { useChatSession } from "../../hooks/useChatSession";
import { MarkdownRenderer } from "./MarkdownRenderer";
import { MCPRenderer } from "../mcp/MCPRenderer";

export function ChatWindow() {
  const { sessionId, setSessionId } = useChatSession();
  const { messages, sendUserMessage, sendAssistantMessage, loading } =
    useChatMessages(sessionId);
  const [input, setInput] = useState("");
  const [thinking, setThinking] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  // ...restante igual...

  // (Opcional: useEffect para atualizar o título da sessão
  // Ouça input/mensagens iniciais e salve como título)

  return (
    <div className="flex flex-col max-w-2xl mx-auto h-[80vh] border rounded shadow bg-white">
      {/* ...restante igual... */}
    </div>
  );
}