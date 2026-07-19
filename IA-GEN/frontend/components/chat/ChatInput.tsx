"use client";

import { useState } from "react";
import Button from "../ui/Button";

interface ChatInputProps {
  onSend: (message: string) => void;
}

export default function ChatInput({ onSend }: ChatInputProps) {
  const [message, setMessage] = useState("");

  function handleSend() {
    console.log("1. handleSend ejecutado");

    if (!message.trim()) return;

    console.log("2. Mensaje:", message);

    onSend(message);

    console.log("3. onSend ejecutado");

    setMessage("");
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "Enter") {
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
          placeholder="Escribe tu pregunta..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
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
          "
        />

        <Button onClick={handleSend}>Enviar</Button>
      </div>
    </div>
  );
}
