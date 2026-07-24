const mobileLinks = [
  {
    label: "Inicio",
    href: "#inicio",
  },
  {
    label: "Cursos",
    href: "#cursos",
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

export default function MobileMenu() {
  return (
    <div
      className="
        absolute
        left-0
        top-full
        h-[calc(100dvh-4.5rem)]
        w-full
        overflow-y-auto
        border-t
        border-white/5
        bg-[#0F172A]
        shadow-[0_24px_60px_rgba(2,6,23,0.65)]
        md:hidden
      "
    >
      <nav
        aria-label="Navegación móvil"
        className="
          mx-auto
          flex
          max-w-7xl
          flex-col
          px-6
          py-5
        "
      >
        <ul className="space-y-1">
          {mobileLinks.map((link) => (
            <li key={link.href}>
              <a
                href={link.href}
                className="
                  flex
                  items-center
                  justify-between
                  rounded-xl
                  px-4
                  py-3.5
                  text-sm
                  font-medium
                  text-[#CBD5E1]
                  outline-none
                  transition-all
                  duration-200
                  hover:bg-white/5
                  hover:text-white
                  focus-visible:bg-white/5
                  focus-visible:ring-2
                  focus-visible:ring-[#2563EB]
                "
              >
                {link.label}

                <span
                  aria-hidden="true"
                  className="
                    text-[#475569]
                    transition-transform
                    duration-200
                  "
                >
                  <ArrowIcon />
                </span>
              </a>
            </li>
          ))}
        </ul>

        <div
          className="
            mt-5
            border-t
            border-white/5
            pt-5
          "
        >
          <a
            href="#chat-ia"
            className="
              flex
              w-full
              items-center
              justify-center
              gap-2
              rounded-xl
              bg-[#2563EB]
              px-5
              py-3.5
              text-sm
              font-semibold
              text-white
              shadow-[0_8px_24px_rgba(37,99,235,0.25)]
              outline-none
              transition-all
              duration-200
              hover:bg-[#1D4ED8]
              focus-visible:ring-2
              focus-visible:ring-[#60A5FA]
              focus-visible:ring-offset-2
              focus-visible:ring-offset-[#0F172A]
            "
          >
            Probar asistente
            <ArrowIcon />
          </a>

          <p
            className="
              mt-4
              text-center
              text-[10px]
              uppercase
              tracking-[0.16em]
              text-[#475569]
            "
          >
            Proyecto educativo con IA
          </p>
        </div>
      </nav>
    </div>
  );
}
