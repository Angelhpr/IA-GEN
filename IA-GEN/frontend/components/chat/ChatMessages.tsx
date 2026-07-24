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
    const container = chatContainerRef.current;

    if (!container) {
      return;
    }

    container.scrollTo({
      top: container.scrollHeight,
      behavior: "smooth",
    });
  }, [messages, isLoading]);

  return (
    <div
      ref={chatContainerRef}
      role="log"
      aria-live="polite"
      aria-relevant="additions text"
      aria-label="Conversación con el asistente IA-GEN"
      className="
        min-h-0
        flex-1
        space-y-5
        overflow-y-auto
        bg-[#0F172A]/35
        px-4
        py-5
        scroll-smooth
        sm:px-5
        sm:py-6
      "
    >
      {messages.map((message, index) => {
        const isUser = message.role === "user";

        return (
          <div
            key={`${message.role}-${index}`}
            className={`
              flex
              w-full
              ${isUser ? "justify-end" : "justify-start"}
            `}
          >
            <div
              className={`
                flex
                max-w-[92%]
                flex-col
                gap-1.5
                sm:max-w-[85%]
                ${isUser ? "items-end" : "items-start"}
              `}
            >
              <span
                className={`
                  px-1
                  text-[10px]
                  font-medium
                  uppercase
                  tracking-[0.14em]
                  ${isUser ? "text-[#60A5FA]" : "text-[#94A3B8]"}
                `}
              >
                {isUser ? "Tú" : "IA-GEN"}
              </span>

              <div
                className={`
                  rounded-2xl
                  px-4
                  py-3
                  text-sm
                  leading-6
                  shadow-sm
                  sm:px-5
                  sm:py-3.5
                  ${
                    isUser
                      ? `
                        rounded-br-sm
                        bg-[#2563EB]
                        text-white
                        shadow-[0_8px_24px_rgba(37,99,235,0.18)]
                      `
                      : `
                        rounded-bl-sm
                        border
                        border-white/5
                        bg-white/5
                        text-[#CBD5E1]
                      `
                  }
                `}
              >
                <p className="whitespace-pre-wrap break-words">
                  {message.content}
                </p>
              </div>
            </div>
          </div>
        );
      })}

      {isLoading && (
        <div role="status" aria-label="IA-GEN está generando una respuesta">
          <TypingIndicator />
        </div>
      )}
    </div>
  );
}
