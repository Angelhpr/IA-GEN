import ChatCard from "./ChatCard";
export default function ChatSection() {
  return (
    <section
      className="
        mx-auto
        max-w-7xl
        px-6
        py-24
      "
    >
      <div
        className="
          grid
          items-center
          gap-16
          lg:grid-cols-2
        "
      >
        {/* Texto izquierdo */}

        <div>
          <p className="font-semibold uppercase tracking-widest text-cyan-400">
            Asistente IA
          </p>

          <h2
            className="
              mt-6
              text-5xl
              font-bold
              leading-tight
            "
          >
            Tu tutor personal.
            <br />
            Disponible 24/7.
          </h2>

          <p
            className="
              mt-8
              max-w-xl
              text-lg
              leading-8
              text-slate-400
            "
          >
            Pregunta sobre cualquier concepto del curso, solicita ejemplos,
            genera código y recibe explicaciones paso a paso gracias al
            asistente inteligente de IA-GEN.
          </p>

          <div className="mt-10 space-y-6">
            <div>⚡ Respuestas instantáneas, 24/7</div>

            <div>📖 Conoce todo el contenido del curso</div>

            <div>{"</>"} Genera y explica código en tiempo real</div>
          </div>
        </div>

        {/* Chat */}

        <div>
          <ChatCard />
        </div>
      </div>
    </section>
  );
}
