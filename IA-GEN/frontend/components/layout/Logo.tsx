interface LogoProps {
  size?: "sm" | "md" | "lg";
}

export default function Logo({ size = "md" }: LogoProps) {
  const sizes = {
    sm: {
      container: "gap-2",
      icon: "h-9 w-9",
      title: "text-base",
      subtitle: "text-[10px]",
    },
    md: {
      container: "gap-2.5",
      icon: "h-11 w-11",
      title: "text-xl",
      subtitle: "text-[11px]",
    },
    lg: {
      container: "gap-3",
      icon: "h-14 w-14",
      title: "text-2xl",
      subtitle: "text-xs",
    },
  };

  const selectedSize = sizes[size];

  return (
    <div
      className={`flex items-center ${selectedSize.container}`}
      aria-label="IA-GEN"
    >
      <div className={`relative shrink-0 ${selectedSize.icon}`}>
        <svg
          viewBox="0 0 36 36"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="h-full w-full"
          aria-hidden="true"
        >
          <rect
            width="36"
            height="36"
            rx="8"
            fill="url(#ia-gen-logo-background)"
          />

          <path
            d="M8 18H13"
            stroke="#93C5FD"
            strokeWidth="1.2"
            strokeLinecap="round"
          />
          <path
            d="M23 18H28"
            stroke="#93C5FD"
            strokeWidth="1.2"
            strokeLinecap="round"
          />
          <path
            d="M18 8V13"
            stroke="#C4B5FD"
            strokeWidth="1.2"
            strokeLinecap="round"
          />
          <path
            d="M18 23V28"
            stroke="#C4B5FD"
            strokeWidth="1.2"
            strokeLinecap="round"
          />

          <path
            d="M10 10L14 14"
            stroke="#93C5FD"
            strokeWidth="1"
            strokeLinecap="round"
            opacity="0.7"
          />
          <path
            d="M22 22L26 26"
            stroke="#93C5FD"
            strokeWidth="1"
            strokeLinecap="round"
            opacity="0.7"
          />
          <path
            d="M26 10L22 14"
            stroke="#C4B5FD"
            strokeWidth="1"
            strokeLinecap="round"
            opacity="0.7"
          />
          <path
            d="M10 26L14 22"
            stroke="#C4B5FD"
            strokeWidth="1"
            strokeLinecap="round"
            opacity="0.7"
          />

          <circle cx="18" cy="18" r="5" fill="url(#ia-gen-logo-core)" />

          <text
            x="18"
            y="21.5"
            textAnchor="middle"
            fontSize="6"
            fontWeight="700"
            fill="white"
            fontFamily="Inter, Arial, sans-serif"
          >
            IA
          </text>

          <circle cx="8" cy="18" r="1.5" fill="#2563EB" />
          <circle cx="28" cy="18" r="1.5" fill="#2563EB" />
          <circle cx="18" cy="8" r="1.5" fill="#7C3AED" />
          <circle cx="18" cy="28" r="1.5" fill="#7C3AED" />

          <circle cx="10" cy="10" r="1" fill="#60A5FA" opacity="0.8" />
          <circle cx="26" cy="10" r="1" fill="#A78BFA" opacity="0.8" />
          <circle cx="10" cy="26" r="1" fill="#A78BFA" opacity="0.8" />
          <circle cx="26" cy="26" r="1" fill="#60A5FA" opacity="0.8" />

          <defs>
            <linearGradient
              id="ia-gen-logo-background"
              x1="0"
              y1="0"
              x2="36"
              y2="36"
              gradientUnits="userSpaceOnUse"
            >
              <stop stopColor="#1E3A8A" />
              <stop offset="1" stopColor="#4C1D95" />
            </linearGradient>

            <linearGradient
              id="ia-gen-logo-core"
              x1="13"
              y1="13"
              x2="23"
              y2="23"
              gradientUnits="userSpaceOnUse"
            >
              <stop stopColor="#2563EB" />
              <stop offset="1" stopColor="#7C3AED" />
            </linearGradient>
          </defs>
        </svg>
      </div>

      <div className="flex flex-col leading-none">
        <span
          className={`
            font-bold
            tracking-tight
            text-white
            ${selectedSize.title}
          `}
        >
          IA
        </span>

        <span
          className={`
            font-semibold
            uppercase
            tracking-[0.2em]
            text-[#94A3B8]
            ${selectedSize.subtitle}
          `}
        >
          GEN
        </span>
      </div>
    </div>
  );
}
