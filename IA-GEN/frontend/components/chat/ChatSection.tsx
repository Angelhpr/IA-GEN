import type { ReactNode } from "react";

import ChatCard from "./ChatCard";

interface Feature {
  title: string;
  description: string;
  icon: ReactNode;
}

const features: Feature[] = [
  {
    title: "Respuestas contextuales",
    description: "Respuestas generadas a partir de la base documental.",
    icon: (
      <svg
        viewBox="0 0 24 24"
        fill="none"
        aria-hidden="true"
        className="h-4 w-4"
      >
        <path
          d="M13 2 5 14h6l-1 8 8-12h-6l1-8Z"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    ),
  },
  {
    title: "Conocimiento documental",
    description: "Consulta la información disponible en IA-GEN mediante RAG.",
    icon: (
      <svg
        viewBox="0 0 24 24"
        fill="none"
        aria-hidden="true"
        className="h-4 w-4"
      >
        <path
          d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5v-16Z"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    ),
  },
  {
    title: "Explicaciones paso a paso",
    description: "Pregunta sobre programación, IA y los contenidos indexados.",
    icon: (
      <svg
        viewBox="0 0 24 24"
        fill="none"
        aria-hidden="true"
        className="h-4 w-4"
      >
        <path
          d="m8 9-3 3 3 3M16 9l3 3-3 3M14 5l-4 14"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    ),
  },
];

export default function ChatSection() {
  return (
    <section
      aria-labelledby="chat-section-title"
      className="
    bg-[#0F172A]
    px-6
    py-16
    md:py-20
  "
    >
      <div
        id="chat-ia"
        className="
          mx-auto
          max-w-7xl
        "
      >
        <div
          className="
            grid
            grid-cols-1
            items-center
            gap-14
            lg:grid-cols-[0.85fr_1.15fr]
            lg:gap-20
          "
        >
          <div>
            <span
              className="
                mb-4
                block
                text-xs
                font-semibold
                uppercase
                tracking-[0.2em]
                text-[#2563EB]
              "
            >
              Asistente IA
            </span>

            <h2
              id="chat-section-title"
              className="
                max-w-xl
                text-3xl
                font-bold
                leading-tight
                tracking-tight
                text-white
                md:text-5xl
              "
            >
              Tu tutor personal.
              <br />
              <span
                className="
                  bg-linear-to-r
                  from-[#2563EB]
                  to-[#7C3AED]
                  bg-clip-text
                  text-transparent
                "
              >
                Siempre listo para ayudarte.
              </span>
            </h2>

            <p
              className="
                mt-6
                max-w-xl
                text-base
                leading-7
                text-[#94A3B8]
                md:text-lg
              "
            >
              Haz preguntas sobre programación, inteligencia artificial y los
              documentos disponibles en IA-GEN. El asistente recupera
              información relevante y genera una respuesta contextual.
            </p>

            <div className="mt-9 space-y-5">
              {features.map((feature) => (
                <div key={feature.title} className="flex items-start gap-4">
                  <div
                    className="
                      mt-0.5
                      flex
                      h-9
                      w-9
                      shrink-0
                      items-center
                      justify-center
                      rounded-xl
                      bg-[#2563EB]/15
                      text-[#60A5FA]
                      ring-1
                      ring-inset
                      ring-[#2563EB]/20
                    "
                  >
                    {feature.icon}
                  </div>

                  <div>
                    <h3 className="text-sm font-semibold text-[#CBD5E1]">
                      {feature.title}
                    </h3>

                    <p className="mt-1 text-sm leading-6 text-[#64748B]">
                      {feature.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            <div
              className="
                mt-10
                inline-flex
                items-center
                gap-2
                rounded-full
                border
                border-emerald-400/15
                bg-emerald-400/5
                px-3
                py-1.5
                text-xs
                text-emerald-400
              "
            >
              <span
                aria-hidden="true"
                className="h-1.5 w-1.5 rounded-full bg-emerald-400"
              />
              Integrado con Gemini y recuperación documental
            </div>
          </div>

          <div className="relative">
            <div
              aria-hidden="true"
              className="
                pointer-events-none
                absolute
                inset-0
                -z-10
                rounded-full
                bg-[#2563EB]/10
                blur-[90px]
              "
            />

            <ChatCard />
          </div>
        </div>
      </div>
    </section>
  );
}
