"use client";

import { FormEvent, useEffect, useRef, useState } from "react";

interface ChatInputProps {
  onSend: (message: string) => void | Promise<void>;
  isLoading: boolean;
}

function SendIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className="h-4 w-4">
      <path
        d="M5 12h14M14 7l5 5-5 5"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

function LoadingIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden="true"
      className="h-4 w-4 animate-spin"
    >
      <circle
        cx="12"
        cy="12"
        r="9"
        stroke="currentColor"
        strokeWidth="2"
        className="opacity-25"
      />

      <path
        d="M21 12a9 9 0 0 0-9-9"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        className="opacity-100"
      />
    </svg>
  );
}

export default function ChatInput({ onSend, isLoading }: ChatInputProps) {
  const [message, setMessage] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  const normalizedMessage = message.trim();
  const cannotSend = isLoading || !normalizedMessage;

  useEffect(() => {
    if (!isLoading) {
      inputRef.current?.focus();
    }
  }, [isLoading]);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (cannotSend) {
      return;
    }

    setMessage("");

    void onSend(normalizedMessage);
  }

  return (
    <footer
      className="
        border-t
        border-white/5
        bg-[#1E293B]
        px-4
        py-3
        sm:px-5
        sm:py-4
      "
    >
      <form
        onSubmit={handleSubmit}
        aria-busy={isLoading}
        className="
          flex
          items-center
          gap-3
        "
      >
        <label htmlFor="ia-gen-chat-input" className="sr-only">
          Escribe una pregunta para el asistente IA-GEN
        </label>

        <div
          className="
            flex
            min-w-0
            flex-1
            items-center
            rounded-xl
            border
            border-white/5
            bg-white/5
            transition-all
            duration-200
            focus-within:border-[#2563EB]/50
            focus-within:bg-white/[0.07]
            focus-within:shadow-[0_0_0_3px_rgba(37,99,235,0.10)]
          "
        >
          <input
            ref={inputRef}
            id="ia-gen-chat-input"
            name="message"
            type="text"
            autoComplete="off"
            maxLength={2000}
            aria-label="Pregunta para el asistente IA-GEN"
            placeholder={
              isLoading ? "Generando respuesta..." : "Escribe tu pregunta..."
            }
            value={message}
            disabled={isLoading}
            onChange={(event) => setMessage(event.target.value)}
            className="
              min-w-0
              flex-1
              bg-transparent
              px-4
              py-3
              text-sm
              text-white
              outline-none
              placeholder:text-[#475569]
              disabled:cursor-not-allowed
              disabled:opacity-60
            "
          />
        </div>

        <button
          type="submit"
          disabled={cannotSend}
          aria-label={isLoading ? "Generando respuesta" : "Enviar pregunta"}
          className="
            flex
            h-11
            w-11
            shrink-0
            items-center
            justify-center
            rounded-xl
            bg-[#2563EB]
            text-white
            shadow-[0_8px_24px_rgba(37,99,235,0.20)]
            outline-none
            transition-all
            duration-200
            hover:bg-[#1D4ED8]
            hover:shadow-[0_0_22px_rgba(37,99,235,0.40)]
            focus-visible:ring-2
            focus-visible:ring-[#60A5FA]
            focus-visible:ring-offset-2
            focus-visible:ring-offset-[#1E293B]
            disabled:cursor-not-allowed
            disabled:opacity-40
            disabled:hover:bg-[#2563EB]
            disabled:hover:shadow-none
          "
        >
          {isLoading ? <LoadingIcon /> : <SendIcon />}
        </button>
      </form>
    </footer>
  );
}
