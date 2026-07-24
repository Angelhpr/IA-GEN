function ArrowIcon() {
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

function GitHubIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className="h-4 w-4">
      <path
        d="M12 2.75a9.25 9.25 0 0 0-2.92 18.03c.46.08.63-.2.63-.44v-1.76c-2.56.56-3.1-1.09-3.1-1.09-.42-1.07-1.03-1.35-1.03-1.35-.84-.58.06-.57.06-.57.93.07 1.42.96 1.42.96.83 1.42 2.17 1.01 2.7.77.08-.6.32-1.01.59-1.24-2.04-.23-4.19-1.02-4.19-4.56 0-1.01.36-1.83.95-2.47-.1-.23-.41-1.17.09-2.44 0 0 .78-.25 2.54.94A8.8 8.8 0 0 1 12 7.16a8.8 8.8 0 0 1 2.31.31c1.76-1.19 2.53-.94 2.53-.94.51 1.27.19 2.21.1 2.44.59.64.95 1.46.95 2.47 0 3.55-2.16 4.32-4.21 4.55.33.29.62.85.62 1.71v2.64c0 .25.17.53.64.44A9.25 9.25 0 0 0 12 2.75Z"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export default function ContactSection() {
  return (
    <section
      aria-labelledby="contact-title"
      className="
        bg-[#0F172A]
        px-5
        py-16
        sm:px-6
        md:py-24
      "
    >
      <div
        id="contacto"
        className="
          mx-auto
          max-w-7xl
        "
      >
        <div
          className="
            relative
            overflow-hidden
            rounded-2xl
            border
            border-white/10
            bg-[#1E293B]
            px-5
            py-10
            text-center
            shadow-[0_24px_70px_rgba(2,6,23,0.35)]
            sm:rounded-3xl
            sm:px-10
            sm:py-14
            md:py-20
          "
        >
          <div
            aria-hidden="true"
            className="
              pointer-events-none
              absolute
              -left-24
              -top-24
              h-72
              w-72
              rounded-full
              bg-[#2563EB]/15
              blur-[100px]
            "
          />

          <div
            aria-hidden="true"
            className="
              pointer-events-none
              absolute
              -bottom-28
              -right-24
              h-72
              w-72
              rounded-full
              bg-[#7C3AED]/15
              blur-[100px]
            "
          />

          <div className="relative mx-auto max-w-3xl">
            <span
              className="
                mb-4
                block
                text-xs
                font-semibold
                uppercase
                tracking-[0.2em]
                text-[#7C3AED]
              "
            >
              Explora el proyecto
            </span>

            <h2
              id="contact-title"
              className="
                text-3xl
                font-bold
                leading-tight
                tracking-tight
                text-white
                md:text-5xl
              "
            >
              Descubre cómo funciona{" "}
              <span
                className="
                  bg-linear-to-r
                  from-[#2563EB]
                  to-[#7C3AED]
                  bg-clip-text
                  text-transparent
                "
              >
                IA-GEN.
              </span>
            </h2>

            <p
              className="
                mx-auto
                mt-6
                max-w-2xl
                text-base
                leading-7
                text-[#94A3B8]
                md:text-lg
              "
            >
              Interactúa con el asistente, consulta la base documental y revisa
              el código utilizado para integrar Next.js, FastAPI, Gemini y
              recuperación aumentada.
            </p>

            <div
              className="
                mt-10
                flex
                flex-col
                items-center
                justify-center
                gap-4
                sm:flex-row
              "
            >
              <a
                href="#chat-ia"
                className="
                  group
                  flex
                  w-full
                  items-center
                  justify-center
                  gap-2
                  rounded-xl
                  bg-[#2563EB]
                  px-7
                  py-3.5
                  text-sm
                  font-semibold
                  text-white
                  shadow-[0_10px_30px_rgba(37,99,235,0.25)]
                  outline-none
                  transition-all
                  duration-200
                  hover:bg-[#1D4ED8]
                  hover:shadow-[0_0_28px_rgba(37,99,235,0.45)]
                  focus-visible:ring-2
                  focus-visible:ring-[#60A5FA]
                  focus-visible:ring-offset-2
                  focus-visible:ring-offset-[#1E293B]
                  sm:w-auto
                "
              >
                Probar asistente
                <span
                  className="
                    transition-transform
                    duration-200
                    group-hover:translate-x-1
                  "
                >
                  <ArrowIcon />
                </span>
              </a>

              <a
                href="https://github.com/Angelhpr/IA-GEN"
                target="_blank"
                rel="noreferrer"
                className="
                  flex
                  w-full
                  items-center
                  justify-center
                  gap-2.5
                  rounded-xl
                  border
                  border-white/10
                  px-7
                  py-3.5
                  text-sm
                  font-semibold
                  text-[#CBD5E1]
                  outline-none
                  transition-all
                  duration-200
                  hover:border-white/20
                  hover:bg-white/5
                  hover:text-white
                  focus-visible:ring-2
                  focus-visible:ring-[#2563EB]
                  focus-visible:ring-offset-2
                  focus-visible:ring-offset-[#1E293B]
                  sm:w-auto
                "
              >
                <GitHubIcon />
                Ver código en GitHub
              </a>
            </div>

            <div
              className="
                mx-auto
                mt-10
                flex
                max-w-xl
                flex-wrap
                items-center
                justify-center
                gap-x-6
                gap-y-3
                border-t
                border-white/5
                pt-7
                text-xs
                text-[#64748B]
              "
            >
              <span>Proyecto personal</span>
              <span aria-hidden="true">•</span>
              <span>Desarrollado para aprendizaje</span>
              <span aria-hidden="true">•</span>
              <span>Código disponible en GitHub</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
