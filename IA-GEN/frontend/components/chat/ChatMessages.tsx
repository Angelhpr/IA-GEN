import { useEffect, useRef } from "react";
import type { Message } from "../../types/message";
import TypingIndicator from "./TypingIndicator";
interface ChatMessagesProps {
  messages: Message[];
  isLoading: boolean;
}

export default function ChatMessages({
  messages,
  isLoading,
}: ChatMessagesProps) {
  const chatContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [messages, isLoading]);
  return (
    <div
      ref={chatContainerRef}
      className="
      min-h-0
      flex-1
      space-y-6
      overflow-y-auto
      p-6
    "
    >
      {messages.map((message, index) => (
        <div
          key={index}
          className={`flex ${
            message.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`
          max-w-[85%]
          rounded-2xl
          px-5
          py-4
        ${
          message.role === "user"
            ? "rounded-tr-sm bg-cyan-500 text-slate-950"
            : "rounded-tl-sm bg-slate-800 text-slate-200"
        }
      `}
          >
            <p>{message.content}</p>
          </div>
        </div>
      ))}
      {isLoading && <TypingIndicator />}
    </div>
  );
}
