"use client";

import { useRef, useState } from "react";

import { ApiError } from "../../lib/api";
import { sendMessage } from "../../services/Chat.services";
import type { Message } from "../../types/message";

import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";

const initialMessages: Message[] = [
  {
    role: "assistant",
    content:
      "¡Hola! Soy el asistente de IA-GEN. Puedo ayudarte con programación, inteligencia artificial y la información disponible en la base documental.",
  },
  {
    role: "assistant",
    content: "¿Qué te gustaría aprender hoy?",
  },
];

function getChatErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    switch (error.code) {
      case "AI_RATE_LIMITED":
        return (
          "He alcanzado temporalmente el límite de solicitudes. " +
          "Inténtalo de nuevo más tarde."
        );

      case "AI_EMPTY_RESPONSE":
        return "No pude generar una respuesta válida. Inténtalo de nuevo.";

      case "AI_CONFIGURATION_ERROR":
        return (
          "El asistente no está disponible en este momento. " +
          "El equipo técnico ya puede revisar el problema."
        );

      case "AI_PROVIDER_ERROR":
      case "AI_SERVICE_UNAVAILABLE":
        return (
          "Ahora mismo el asistente no está disponible. " +
          "Inténtalo de nuevo más tarde."
        );

      default:
        if (error.status >= 500) {
          return (
            "El servidor tuvo un problema al procesar tu pregunta. " +
            "Inténtalo nuevamente."
          );
        }
    }
  }

  if (error instanceof TypeError) {
    return (
      "No pude conectarme con el servidor. " +
      "Comprueba tu conexión e inténtalo nuevamente."
    );
  }

  return "Ocurrió un problema inesperado. Inténtalo nuevamente.";
}

function AssistantIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden="true"
      className="h-4 w-4 text-white"
    >
      <path
        d="M9.5 5.5A3.5 3.5 0 0 1 13 2a3.5 3.5 0 0 1 3.36 2.52A3.5 3.5 0 0 1 18 11v3a4 4 0 0 1-4 4h-1v3"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
        strokeLinejoin="round"
      />

      <path
        d="M10 22v-4H9a4 4 0 0 1-4-4v-3a3.5 3.5 0 0 1 1.64-6.48A3.5 3.5 0 0 1 10 2"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
        strokeLinejoin="round"
      />

      <path
        d="M9 8.5h6M9 12h6"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
      />
    </svg>
  );
}

export default function ChatCard() {
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [isLoading, setIsLoading] = useState(false);

  const requestInFlightRef = useRef(false);

  function appendMessage(role: Message["role"], content: string) {
    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role,
        content,
      },
    ]);
  }

  async function handleUserMessage(content: string): Promise<void> {
    const normalizedContent = content.trim();

    if (requestInFlightRef.current || !normalizedContent) {
      return;
    }

    requestInFlightRef.current = true;

    appendMessage("user", normalizedContent);
    setIsLoading(true);

    try {
      const answer = await sendMessage(normalizedContent);

      appendMessage("assistant", answer);
    } catch (error: unknown) {
      console.error("Error al enviar el mensaje:", error);

      appendMessage("assistant", getChatErrorMessage(error));
    } finally {
      requestInFlightRef.current = false;
      setIsLoading(false);
    }
  }

  return (
    <div
      role="region"
      aria-label="Chat con el asistente IA-GEN"
      className="
        flex
        h-[520px]
        min-h-0
        flex-col
        overflow-hidden
        rounded-2xl
        border
        border-white/10
        bg-[#1E293B]
        shadow-[0_24px_70px_rgba(2,6,23,0.45)]
        md:h-[560px]
        lg:h-[540px]
      "
    >
      <header
        className="
          flex
          items-center
          justify-between
          border-b
          border-white/5
          bg-[#1E293B]/95
          px-5
          py-4
        "
      >
        <div className="flex items-center gap-3">
          <div
            className="
              flex
              h-9
              w-9
              shrink-0
              items-center
              justify-center
              rounded-full
              bg-gradient-to-br
              from-[#2563EB]
              to-[#7C3AED]
              shadow-[0_0_20px_rgba(124,58,237,0.25)]
            "
          >
            <AssistantIcon />
          </div>

          <div>
            <h3 className="text-sm font-semibold text-white">
              Asistente IA-GEN
            </h3>

            <p
              className="
                mt-0.5
                flex
                items-center
                gap-1.5
                text-[11px]
                text-emerald-400
              "
            >
              <span
                aria-hidden="true"
                className="h-1.5 w-1.5 rounded-full bg-emerald-400"
              />

              {isLoading ? "Generando respuesta..." : "Listo para ayudarte"}
            </p>
          </div>
        </div>

        <div
          className="
            hidden
            items-center
            gap-2
            rounded-full
            border
            border-white/5
            bg-white/5
            px-3
            py-1.5
            text-[10px]
            font-medium
            text-[#94A3B8]
            sm:flex
          "
        >
          <span className="text-[#60A5FA]">RAG</span>
          <span aria-hidden="true">+</span>
          <span className="text-[#A78BFA]">Gemini</span>
        </div>
      </header>

      <ChatMessages messages={messages} isLoading={isLoading} />

      <ChatInput onSend={handleUserMessage} isLoading={isLoading} />
    </div>
  );
}
