interface FeatureCardProps {
  emoji: string;
  title: string;
  description: string;
}

export default function FeatureCard({
  emoji,
  title,
  description,
}: FeatureCardProps) {
  return (
    <div
      className="
        rounded-2xl
        border
        border-cyan-500/20
        bg-slate-900
        p-8
        text-center
        transition
        duration-300
        hover:-translate-y-2
        hover:border-cyan-400
        hover:shadow-cyan-500/20
        hover:shadow-2xl
      "
    >
      <div className="text-5xl">{emoji}</div>

      <h3 className="mt-6 text-xl font-bold text-cyan-400">{title}</h3>

      <p className="mt-4 text-slate-300">{description}</p>
    </div>
  );
}
