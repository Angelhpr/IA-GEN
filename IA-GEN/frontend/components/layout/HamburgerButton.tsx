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
      type="button"
      onClick={onClick}
      aria-label={
        isOpen ? "Cerrar menú de navegación" : "Abrir menú de navegación"
      }
      aria-expanded={isOpen}
      className="
        flex
        h-11
        w-11
        items-center
        justify-center
        rounded-xl
        border
        border-white/10
        bg-white/3
        text-[#CBD5E1]
        outline-none
        transition-all
        duration-200
        hover:border-white/20
        hover:bg-white/[0.07]
        hover:text-white
        focus-visible:ring-2
        focus-visible:ring-[#2563EB]
        focus-visible:ring-offset-2
        focus-visible:ring-offset-[#0F172A]
        md:hidden
      "
    >
      <svg
        viewBox="0 0 24 24"
        fill="none"
        aria-hidden="true"
        className="
          h-5
          w-5
          transition-transform
          duration-200
        "
      >
        {isOpen ? (
          <path
            d="M6 6 18 18M18 6 6 18"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
          />
        ) : (
          <path
            d="M4 7h16M4 12h16M4 17h16"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
          />
        )}
      </svg>
    </button>
  );
}
