interface BadgeProps {
  children: React.ReactNode;
}

export default function Badge({
  children,
}: BadgeProps) {
  return (
    <span
      className="
        rounded-full
        border
        border-cyan-400/30
        bg-slate-800
        px-4
        py-2
        text-sm
        text-cyan-300
      "
    >
      {children}
    </span>
  );
}