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

function PlayIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className="h-4 w-4">
      <path
        d="m9 7 8 5-8 5V7Z"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

function SparklesIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" className="h-4 w-4">
      <path
        d="m12 3 1.2 3.3L16.5 7.5l-3.3 1.2L12 12l-1.2-3.3-3.3-1.2 3.3-1.2L12 3ZM18 13l.8 2.2L21 16l-2.2.8L18 19l-.8-2.2L15 16l2.2-.8L18 13ZM6 14l.8 2.2L9 17l-2.2.8L6 20l-.8-2.2L3 17l2.2-.8L6 14Z"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

const projectHighlights = [
  {
    value: "4",
    label: "Rutas de aprendizaje",
  },
  {
    value: "RAG",
    label: "Contexto documental",
  },
  {
    value: "Gemini",
    label: "Asistente integrado",
  },
];

export default function Hero() {
  return (
    <section
      id="inicio"
      aria-labelledby="hero-title"
      className="
        relative
        flex
        min-h-[calc(100svh-4rem)]
        scroll-mt-16
        items-center
        justify-center
        overflow-hidden
        bg-[#0F172A]
        px-6
        py-20
        md:py-24
      "
    >
      <div
        aria-hidden="true"
        className="
          pointer-events-none
          absolute
          inset-0
          overflow-hidden
        "
      >
        <div
          className="
            absolute
            left-1/2
            top-1/4
            h-130
            w-190
            -translate-x-1/2
            rounded-full
            bg-[#2563EB]/10
            blur-[120px]
          "
        />

        <div
          className="
            absolute
            left-1/3
            top-1/3
            h-105
            w-125
            rounded-full
            bg-[#7C3AED]/10
            blur-[110px]
          "
        />
        <div
          className="
            absolute
            inset-x-0
            bottom-0
            h-52
            bg-linear-to-b
            from-transparent
            via-[#0F172A]/75
            to-[#0F172A]
          "
        />

        <div
          className="
            absolute
            left-1/2
            top-1/4
            h-130
            w-190
            -translate-x-1/2
            rounded-full
            bg-[#2563EB]/10
            blur-[120px]
          "
        />

        <div
          className="
            absolute
            left-1/3
            top-1/3
            h-105
            w-125
            rounded-full
            bg-[#7C3AED]/10
            blur-[110px]
          "
        />
      </div>

      <div
        className="
          relative
          z-10
          mx-auto
          w-full
          max-w-5xl
          text-center
        "
      >
        <div
          className="
            mb-8
            inline-flex
            items-center
            gap-2
            rounded-full
            border
            border-white/10
            bg-white/5
            px-4
            py-1.5
            text-xs
            font-medium
            text-[#94A3B8]
            backdrop-blur-sm
          "
        >
          <span className="text-[#A78BFA]">
            <SparklesIcon />
          </span>
          Proyecto educativo con IA generativa
        </div>

        <h1
          id="hero-title"
          className="
            text-5xl
            font-extrabold
            leading-[1.05]
            tracking-tight
            text-white
            sm:text-6xl
            md:text-7xl
          "
        >
          Aprende IA.{" "}
          <span
            className="
              bg-linear-to-r
              from-[#2563EB]
              via-[#4F46E5]
              to-[#7C3AED]
              bg-clip-text
              text-transparent
            "
          >
            Construye el futuro.
          </span>
        </h1>

        <p
          className="
            mx-auto
            mt-7
            max-w-3xl
            text-base
            leading-8
            text-[#94A3B8]
            sm:text-lg
            md:text-xl
          "
        >
          Explora programación, inteligencia artificial, aprendizaje automático
          y servicios en la nube con recursos prácticos y un asistente conectado
          a una base documental.
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
              hover:shadow-[0_0_30px_rgba(37,99,235,0.45)]
              focus-visible:ring-2
              focus-visible:ring-[#60A5FA]
              focus-visible:ring-offset-2
              focus-visible:ring-offset-[#0F172A]
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
            href="#cursos"
            className="
              group
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
              focus-visible:ring-offset-[#0F172A]
              sm:w-auto
            "
          >
            <span className="text-[#60A5FA]">
              <PlayIcon />
            </span>
            Explorar cursos
          </a>
        </div>

        <div
          className="
            mx-auto
            mt-16
            grid
            max-w-2xl
            grid-cols-1
            gap-6
            sm:grid-cols-3
            sm:gap-8
            md:mt-20
          "
        >
          {projectHighlights.map((highlight) => (
            <div
              key={highlight.label}
              className="
                flex
                flex-col
                items-center
                rounded-2xl
                border
                border-white/5
                bg-white/2.5
                px-4
                py-5
                backdrop-blur-sm
                sm:border-0
                sm:bg-transparent
                sm:px-2
                sm:py-0
              "
            >
              <span
                className="
                  text-2xl
                  font-bold
                  text-white
                  md:text-3xl
                "
              >
                {highlight.value}
              </span>

              <span
                className="
                  mt-1
                  text-xs
                  leading-5
                  text-[#64748B]
                "
              >
                {highlight.label}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
