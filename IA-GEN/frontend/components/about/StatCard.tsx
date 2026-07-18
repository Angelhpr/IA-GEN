interface StatCardProps {
  value: string;
  label: string;
}

export default function StatCard({ value, label }: StatCardProps) {
  return (
    <div
      className="
        rounded-2xl
        border
        border-cyan-500/20
        bg-slate-900
        p-6
        text-center
      "
    >
      <h3 className="text-4xl font-bold text-cyan-400">{value}</h3>

      <p className="mt-2 text-slate-300">{label}</p>
    </div>
  );
}
