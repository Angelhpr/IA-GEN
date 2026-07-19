"use client";

import { useState } from "react";

import Button from "../ui/Button";

interface ChatInputProps {
  onSend: (message: string) => void | Promise<void>;
  isLoading: boolean;
}

export default function ChatInput({ onSend, isLoading }: ChatInputProps) {
  const [message, setMessage] = useState("");

  function handleSend() {
    const normalizedMessage = message.trim();

    if (isLoading || !normalizedMessage) {
      return;
    }

    setMessage("");

    void onSend(normalizedMessage);
  }

  function handleKeyDown(event: React.KeyboardEvent<HTMLInputElement>) {
    if (event.key === "Enter") {
      event.preventDefault();
      handleSend();
    }
  }

  return (
    <div
      className="
        border-t
        border-cyan-500/10
        p-5
      "
    >
      <div className="flex gap-4">
        <input
          type="text"
          aria-label="Pregunta para el asistente IA-GEN"
          placeholder={
            isLoading ? "Esperando respuesta..." : "Escribe tu pregunta..."
          }
          value={message}
          disabled={isLoading}
          onChange={(event) => setMessage(event.target.value)}
          onKeyDown={handleKeyDown}
          className="
            flex-1
            rounded-xl
            border
            border-slate-700
            bg-slate-800
            px-4
            py-3
            text-slate-200
            outline-none
            transition
            focus:border-cyan-400
            disabled:cursor-not-allowed
            disabled:opacity-60
          "
        />

        <Button onClick={handleSend} disabled={isLoading}>
          {isLoading ? "Enviando..." : "Enviar"}
        </Button>
      </div>
    </div>
  );
}
