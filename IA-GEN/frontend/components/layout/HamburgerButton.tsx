interface HamburgerButtonProps {
  isOpen: boolean;
  onClick: () => void;
}

export default function HamburgerButton({
  isOpen,
  onClick,
}: HamburgerButtonProps) {
  return (
    <button
      onClick={onClick}
      className="
        flex
        h-11
        w-11
        items-center
        justify-center
        rounded-lg
        border
        border-cyan-500/20
        text-cyan-400
        transition-colors
        hover:bg-cyan-500/10
      "
      aria-label={isOpen ? "Cerrar menú" : "Abrir menú"}
    >
      <span className="text-2xl">{isOpen ? "✕" : "☰"}</span>
    </button>
  );
}
