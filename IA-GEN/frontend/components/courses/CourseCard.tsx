import Button from "../ui/Button";

interface CourseCardProps {
  emoji: string;
  title: string;
  description: string;
  level: string;
}

export default function CourseCard({
  emoji,
  title,
  description,
  level,
}: CourseCardProps) {
  return (
    <div
      className="
      rounded-2xl
      border
      border-cyan-500/20
      bg-slate-900
      p-8
      transition
      duration-300
      hover:border-cyan-400
      hover:-translate-y-2
      hover:shadow-cyan-500/20
      hover:shadow-2xl
    "
    >
      <div className="mb-6">
        <span
          className="
          rounded-full
          border
          border-cyan-400/30
          bg-cyan-500/10
          px-3
          py-1
          text-xs
          font-medium
          text-cyan-300
        "
        >
          {level}
        </span>
      </div>

      <div className="text-5xl">{emoji}</div>

      <h3 className="mt-6 text-2xl font-bold text-cyan-400">{title}</h3>

      <p className="mt-4 text-slate-300">{description}</p>

      <div className="mt-8">
        <Button variant="secondary">Ver curso</Button>
      </div>
    </div>
  );
}
