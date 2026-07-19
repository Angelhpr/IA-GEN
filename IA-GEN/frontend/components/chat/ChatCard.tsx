"use client";

import { useRef, useState } from "react";

import { ApiError } from "../../lib/api";
import { sendMessage } from "../../services/Chat.services";
import type { Message } from "../../types/message";

import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";

function getChatErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    switch (error.code) {
      case "AI_RATE_LIMITED":
        return (
          "He alcanzado temporalmente el límite de solicitudes. " +
          "Inténtalo de nuevo más tarde."
        );

      case "AI_EMPTY_RESPONSE":
        return "No pude generar una respuesta válida. " + "Inténtalo de nuevo.";

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

  return "Ocurrió un problema inesperado. " + "Inténtalo nuevamente.";
}

export default function ChatCard() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "¡Hola! 👋",
    },
    {
      role: "assistant",
      content:
        "Estoy listo para ayudarte con cualquier duda sobre nuestros cursos, programación, Inteligencia Artificial o Cloud Computing.",
    },
    {
      role: "assistant",
      content: "¿Qué te gustaría aprender hoy?",
    },
  ]);

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
    if (requestInFlightRef.current) {
      return;
    }

    requestInFlightRef.current = true;

    appendMessage("user", content.trim());

    setIsLoading(true);

    try {
      const answer = await sendMessage(content);

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
      className="
        flex
        h-[620px]
        flex-col
        rounded-3xl
        border
        border-cyan-500/20
        bg-slate-900
        shadow-2xl
      "
    >
      <div
        className="
          flex
          items-center
          justify-between
          border-b
          border-cyan-500/10
          px-6
          py-5
        "
      >
        <div>
          <h3 className="font-semibold text-cyan-400">Asistente IA-GEN</h3>

          <p className="text-sm text-green-400">● En línea</p>
        </div>

        <div className="text-3xl">🤖</div>
      </div>

      <ChatMessages messages={messages} isLoading={isLoading} />

      <ChatInput onSend={handleUserMessage} isLoading={isLoading} />
    </div>
  );
}
