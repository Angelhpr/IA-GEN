interface FloatingCardProps {
  children: React.ReactNode;
  position: string;
}

export default function FloatingCard({
  children,
  position,
}: FloatingCardProps) {
  return (
    <div
      className={`
        absolute
        ${position}
        rounded-xl
        border
        border-cyan-400/20
        bg-slate-900/80
        px-4
        py-2
        text-xs
        text-cyan-300
        shadow-lg
      `}
    >
      {children}
    </div>
  );
}
