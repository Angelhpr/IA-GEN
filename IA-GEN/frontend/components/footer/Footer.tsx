import Logo from "../layout/Logo";

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

const navigationLinks = [
  {
    label: "Inicio",
    href: "#inicio",
  },
  {
    label: "Cursos",
    href: "#cursos",
  },
  {
    label: "Características",
    href: "#caracteristicas",
  },
  {
    label: "Sobre el proyecto",
    href: "#nosotros",
  },
  {
    label: "Chat IA",
    href: "#chat-ia",
  },
  {
    label: "Contacto",
    href: "#contacto",
  },
];

const technologies = [
  "Next.js",
  "FastAPI",
  "Gemini",
  "RAG",
  "ChromaDB",
  "Python",
];

export default function Footer() {
  return (
    <footer
      aria-label="Pie de página"
      className="
        border-t
        border-white/5
        bg-[#080E1A]
      "
    >
      <div
        className="
          mx-auto
          grid
          max-w-7xl
          grid-cols-1
          gap-12
          px-6
          py-16
          md:grid-cols-[1.3fr_0.8fr_1fr]
          md:gap-16
          lg:py-20
        "
      >
        <div>
          <a
            href="#inicio"
            aria-label="Volver al inicio de IA-GEN"
            className="
              inline-flex
              rounded-lg
              outline-none
              focus-visible:ring-2
              focus-visible:ring-[#2563EB]
              focus-visible:ring-offset-4
              focus-visible:ring-offset-[#080E1A]
            "
          >
            <Logo size="sm" />
          </a>

          <p
            className="
              mt-5
              max-w-sm
              text-sm
              leading-7
              text-[#64748B]
            "
          >
            Proyecto educativo que integra programación, inteligencia artificial
            y recuperación documental en una experiencia web funcional.
          </p>

          <a
            href="https://github.com/Angelhpr/IA-GEN"
            target="_blank"
            rel="noreferrer"
            className="
              mt-7
              inline-flex
              items-center
              gap-2
              rounded-lg
              border
              border-white/5
              bg-white/[0.025]
              px-4
              py-2.5
              text-xs
              font-medium
              text-[#94A3B8]
              outline-none
              transition-all
              duration-200
              hover:border-white/10
              hover:bg-white/5
              hover:text-white
              focus-visible:ring-2
              focus-visible:ring-[#2563EB]
              focus-visible:ring-offset-2
              focus-visible:ring-offset-[#080E1A]
            "
          >
            <GitHubIcon />
            Repositorio en GitHub
          </a>
        </div>

        <nav aria-label="Navegación del pie de página">
          <h2
            className="
              text-xs
              font-semibold
              uppercase
              tracking-[0.18em]
              text-white
            "
          >
            Navegación
          </h2>

          <ul className="mt-6 grid grid-cols-2 gap-x-5 gap-y-4 md:grid-cols-1">
            {navigationLinks.map((link) => (
              <li key={link.href}>
                <a
                  href={link.href}
                  className="
                    text-sm
                    text-[#64748B]
                    outline-none
                    transition-colors
                    duration-200
                    hover:text-[#60A5FA]
                    focus-visible:text-[#60A5FA]
                  "
                >
                  {link.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div>
          <h2
            className="
              text-xs
              font-semibold
              uppercase
              tracking-[0.18em]
              text-white
            "
          >
            Tecnologías
          </h2>

          <div className="mt-6 flex flex-wrap gap-2.5">
            {technologies.map((technology) => (
              <span
                key={technology}
                className="
                  rounded-full
                  border
                  border-white/5
                  bg-white/[0.025]
                  px-3.5
                  py-2
                  text-xs
                  text-[#64748B]
                "
              >
                {technology}
              </span>
            ))}
          </div>

          <div
            className="
              mt-8
              rounded-2xl
              border
              border-white/5
              bg-white/[0.02]
              p-4
            "
          >
            <div className="flex items-center gap-2">
              <span
                aria-hidden="true"
                className="
                  h-2
                  w-2
                  rounded-full
                  bg-emerald-400
                  shadow-[0_0_10px_rgba(52,211,153,0.65)]
                "
              />

              <span className="text-xs font-medium text-[#CBD5E1]">
                Proyecto funcional
              </span>
            </div>

            <p className="mt-2 text-xs leading-5 text-[#475569]">
              Desarrollado con fines educativos y de aprendizaje.
            </p>
          </div>
        </div>
      </div>
      <div className="border-t border-white/5">
        <div
          className="
            mx-auto
            flex
            max-w-7xl
            flex-col
            items-center
            justify-between
            gap-3
            px-6
            py-6
            text-center
            text-xs
            text-[#475569]
            sm:flex-row
            sm:text-left
          "
        >
          <p>© 2026 IA-GEN. Proyecto educativo.</p>

          <p>Next.js · FastAPI · Gemini · RAG</p>
        </div>
      </div>
    </footer>
  );
}
