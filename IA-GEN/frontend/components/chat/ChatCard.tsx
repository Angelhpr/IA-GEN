"use client";
import { useState } from "react";
import ChatMessages from "./ChatMessages";
import ChatInput from "./ChatInput";
import type { Message } from "../../types/message";
import { sendMessage } from "../../services/Chat.services";

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

  function appendMessage(role: Message["role"], content: string) {
    setMessages((prev) => [
      ...prev,
      {
        role,
        content,
      },
    ]);
  }

  async function handleUserMessage(content: string) {
    appendMessage("user", content);

    const answer = await sendMessage(content);

    appendMessage("assistant", answer);
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
      {/* Header */}
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
      {/* Aquí irán los mensajes */}
      <ChatMessages messages={messages} />
      {/* Input */}
      <ChatInput onSend={handleUserMessage} />
    </div>
  );
}
