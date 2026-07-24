interface FeatureCardProps {
  emoji: string;
  title: string;
  description: string;
  index: number;
}

const accentStyles = [
  {
    icon: "bg-blue-400/10 ring-blue-400/20",
    glow: "bg-[#2563EB]/10",
    number: "text-blue-400",
    title: "group-hover:text-blue-300",
  },
  {
    icon: "bg-purple-400/10 ring-purple-400/20",
    glow: "bg-[#7C3AED]/10",
    number: "text-purple-400",
    title: "group-hover:text-purple-300",
  },
  {
    icon: "bg-cyan-400/10 ring-cyan-400/20",
    glow: "bg-cyan-400/10",
    number: "text-cyan-400",
    title: "group-hover:text-cyan-300",
  },
  {
    icon: "bg-emerald-400/10 ring-emerald-400/20",
    glow: "bg-emerald-400/10",
    number: "text-emerald-400",
    title: "group-hover:text-emerald-300",
  },
];

export default function FeatureCard({
  emoji,
  title,
  description,
  index,
}: FeatureCardProps) {
  const styles = accentStyles[index % accentStyles.length];

  return (
    <article
      className="
        group
        relative
        flex
        min-h-[280px]
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
        className={`
          pointer-events-none
          absolute
          -right-14
          -top-14
          h-32
          w-32
          rounded-full
          blur-3xl
          opacity-60
          transition-opacity
          duration-300
          group-hover:opacity-100
          ${styles.glow}
        `}
      />

      <div className="relative flex items-start justify-between">
        <div
          aria-hidden="true"
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
        >
          {emoji}
        </div>

        <span
          className={`
            text-xs
            font-semibold
            tracking-[0.15em]
            ${styles.number}
          `}
        >
          {String(index + 1).padStart(2, "0")}
        </span>
      </div>

      <div className="relative mt-8">
        <h3
          className={`
            text-xl
            font-semibold
            leading-snug
            text-white
            transition-colors
            duration-200
            ${styles.title}
          `}
        >
          {title}
        </h3>

        <p className="mt-4 text-sm leading-6 text-[#94A3B8]">{description}</p>
      </div>

      <div
        className="
          relative
          mt-auto
          border-t
          border-white/5
          pt-5
        "
      >
        <span
          className="
            text-[10px]
            font-semibold
            uppercase
            tracking-[0.18em]
            text-[#64748B]
          "
        >
          IA-GEN
        </span>
      </div>
    </article>
  );
}
