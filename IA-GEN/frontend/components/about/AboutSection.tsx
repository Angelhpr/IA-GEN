const technologies = [
  {
    number: "01",
    title: "Next.js",
    description:
      "Interfaz web moderna, responsive y preparada para desplegarse en Vercel.",
    color: "text-blue-400",
    background: "bg-blue-400/10",
    ring: "ring-blue-400/20",
  },
  {
    number: "02",
    title: "FastAPI",
    description:
      "Backend encargado de procesar las preguntas y coordinar los servicios de IA.",
    color: "text-emerald-400",
    background: "bg-emerald-400/10",
    ring: "ring-emerald-400/20",
  },
  {
    number: "03",
    title: "Gemini",
    description:
      "Modelo generativo utilizado para construir respuestas claras y contextuales.",
    color: "text-purple-400",
    background: "bg-purple-400/10",
    ring: "ring-purple-400/20",
  },
  {
    number: "04",
    title: "RAG documental",
    description:
      "Recuperación de información desde una base vectorial antes de generar cada respuesta.",
    color: "text-blue-400",
    background: "bg-blue-400/10",
    ring: "ring-blue-400/20",
  },
];

function CheckIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className="h-4 w-4">
      <path
        d="m5 12 4 4L19 6"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export default function AboutSection() {
  return (
    <section
      aria-labelledby="about-title"
      className="
    bg-[#0F172A]
    px-6
    py-16
    md:py-24
  "
    >
      <div
        id="nosotros"
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
            lg:grid-cols-[0.9fr_1.1fr]
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
              Sobre el proyecto
            </span>

            <h2
              id="about-title"
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
              Una experiencia educativa construida alrededor de la{" "}
              <span
                className="
                  bg-linear-to-r
                  from-[#2563EB]
                  to-[#7C3AED]
                  bg-clip-text
                  text-transparent
                "
              >
                inteligencia artificial.
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
              IA-GEN es un proyecto personal desarrollado como parte de un
              proceso de aprendizaje. Integra una aplicación web, un backend en
              Python y un asistente capaz de consultar una base documental.
            </p>

            <p className="mt-5 max-w-xl text-sm leading-7 text-[#64748B]">
              El objetivo no es simular una plataforma comercial, sino demostrar
              cómo distintas tecnologías pueden combinarse para construir una
              aplicación de inteligencia artificial funcional.
            </p>

            <div className="mt-9 space-y-4">
              {[
                "Interfaz responsive construida con componentes reutilizables.",
                "Backend desacoplado y preparado para despliegue independiente.",
                "Respuestas enriquecidas mediante recuperación documental.",
              ].map((item) => (
                <div key={item} className="flex items-start gap-3">
                  <span
                    className="
                      mt-0.5
                      flex
                      h-6
                      w-6
                      shrink-0
                      items-center
                      justify-center
                      rounded-full
                      bg-[#2563EB]/15
                      text-[#60A5FA]
                    "
                  >
                    <CheckIcon />
                  </span>

                  <span className="text-sm leading-6 text-[#CBD5E1]">
                    {item}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <div
            className="
              relative
              overflow-hidden
              rounded-3xl
              border
              border-white/5
              bg-[#0D1526]
              p-5
              shadow-[0_24px_70px_rgba(2,6,23,0.35)]
              sm:p-7
            "
          >
            <div
              aria-hidden="true"
              className="
                pointer-events-none
                absolute
                -right-24
                -top-24
                h-64
                w-64
                rounded-full
                bg-[#7C3AED]/10
                blur-[90px]
              "
            />

            <div
              aria-hidden="true"
              className="
                pointer-events-none
                absolute
                -bottom-24
                -left-24
                h-64
                w-64
                rounded-full
                bg-[#2563EB]/10
                blur-[90px]
              "
            />

            <div className="relative">
              <div
                className="
                  mb-6
                  flex
                  items-center
                  justify-between
                  border-b
                  border-white/5
                  pb-5
                "
              >
                <div>
                  <span
                    className="
                      text-[10px]
                      font-semibold
                      uppercase
                      tracking-[0.18em]
                      text-[#64748B]
                    "
                  >
                    Arquitectura
                  </span>

                  <h3 className="mt-1 text-lg font-semibold text-white">
                    Cómo funciona IA-GEN
                  </h3>
                </div>

                <span
                  className="
                    rounded-full
                    border
                    border-emerald-400/15
                    bg-emerald-400/5
                    px-3
                    py-1.5
                    text-[10px]
                    font-medium
                    text-emerald-400
                  "
                >
                  Proyecto funcional
                </span>
              </div>

              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                {technologies.map((technology) => (
                  <article
                    key={technology.title}
                    className="
                      rounded-2xl
                      border
                      border-white/5
                      bg-white/2.5
                      p-5
                      transition-all
                      duration-300
                      hover:border-white/10
                      hover:bg-white/4.5
                    "
                  >
                    <div className="flex items-center justify-between">
                      <div
                        className={`
                          flex
                          h-10
                          w-10
                          items-center
                          justify-center
                          rounded-xl
                          text-xs
                          font-bold
                          ring-1
                          ring-inset
                          ${technology.color}
                          ${technology.background}
                          ${technology.ring}
                        `}
                      >
                        {technology.number}
                      </div>

                      <span
                        aria-hidden="true"
                        className="text-sm text-[#334155]"
                      >
                        ↗
                      </span>
                    </div>

                    <h4 className="mt-5 font-semibold text-white">
                      {technology.title}
                    </h4>

                    <p className="mt-2 text-sm leading-6 text-[#64748B]">
                      {technology.description}
                    </p>
                  </article>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
