interface CourseCardProps {
  emoji: string;
  title: string;
  description: string;
  level: string;
}

const levelStyles: Record<
  string,
  {
    badge: string;
    icon: string;
    accent: string;
  }
> = {
  "Nivel inicial": {
    badge: "bg-emerald-400/10 text-emerald-400",
    icon: "bg-emerald-400/10 ring-emerald-400/20",
    accent: "group-hover:text-emerald-300",
  },
  Intermedio: {
    badge: "bg-blue-400/10 text-blue-400",
    icon: "bg-blue-400/10 ring-blue-400/20",
    accent: "group-hover:text-blue-300",
  },
  Avanzado: {
    badge: "bg-purple-400/10 text-purple-400",
    icon: "bg-purple-400/10 ring-purple-400/20",
    accent: "group-hover:text-purple-300",
  },
  Profesional: {
    badge: "bg-amber-400/10 text-amber-400",
    icon: "bg-amber-400/10 ring-amber-400/20",
    accent: "group-hover:text-amber-300",
  },
};

const fallbackStyles = {
  badge: "bg-[#2563EB]/10 text-[#60A5FA]",
  icon: "bg-[#2563EB]/10 ring-[#2563EB]/20",
  accent: "group-hover:text-[#93C5FD]",
};

export default function CourseCard({
  emoji,
  title,
  description,
  level,
}: CourseCardProps) {
  const styles = levelStyles[level] ?? fallbackStyles;

  return (
    <article
      className="
        group
        relative
        flex
        min-h-[310px]
        flex-col
        overflow-hidden
        rounded-2xl
        border
        border-white/5
        bg-[#1E293B]
        p-6
        transition-all
        duration-300
        hover:-translate-y-1
        hover:border-white/10
        hover:bg-[#243044]
        hover:shadow-[0_20px_50px_rgba(2,6,23,0.35)]
      "
    >
      <div
        aria-hidden="true"
        className="
          pointer-events-none
          absolute
          -right-16
          -top-16
          h-36
          w-36
          rounded-full
          bg-[#2563EB]/5
          blur-3xl
          transition-opacity
          duration-300
          group-hover:opacity-100
        "
      />

      <div className="relative flex items-start justify-between gap-4">
        <div
          className={`
            flex
            h-12
            w-12
            items-center
            justify-center
            rounded-xl
            text-2xl
            ring-1
            ring-inset
            ${styles.icon}
          `}
          aria-hidden="true"
        >
          {emoji}
        </div>

        <span
          className={`
            rounded-full
            px-3
            py-1
            text-[11px]
            font-medium
            ${styles.badge}
          `}
        >
          {level}
        </span>
      </div>

      <div className="relative mt-8">
        <span
          className="
            text-[10px]
            font-semibold
            uppercase
            tracking-[0.18em]
            text-[#64748B]
          "
        >
          Ruta de aprendizaje
        </span>

        <h3
          className={`
            mt-2
            text-xl
            font-semibold
            leading-snug
            text-white
            transition-colors
            duration-200
            ${styles.accent}
          `}
        >
          {title}
        </h3>

        <p className="mt-3 text-sm leading-6 text-[#94A3B8]">{description}</p>
      </div>

      <div
        className="
          relative
          mt-auto
          flex
          items-center
          justify-between
          border-t
          border-white/5
          pt-5
          text-xs
          text-[#64748B]
        "
      >
        <span>Aprendizaje basado en proyectos</span>

        <span
          aria-hidden="true"
          className="
            text-base
            text-[#2563EB]
            opacity-40
            transition-all
            duration-200
            group-hover:translate-x-1
            group-hover:opacity-100
          "
        >
          →
        </span>
      </div>
    </article>
  );
}
