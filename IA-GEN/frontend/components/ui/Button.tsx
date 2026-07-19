import type { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  variant?: "primary" | "secondary";
  size?: "sm" | "md" | "lg";
}

export default function Button({
  children,
  variant = "primary",
  size = "md",
  type = "button",
  className = "",
  ...buttonProps
}: ButtonProps) {
  const styles = {
    primary: "bg-cyan-500 text-slate-950 hover:bg-cyan-400",

    secondary:
      "border border-cyan-500 text-cyan-400 hover:bg-cyan-500 hover:text-slate-950",
  };

  const sizes = {
    sm: "px-4 py-2 text-sm",
    md: "px-6 py-3 text-base",
    lg: "px-8 py-4 text-lg",
  };

  return (
    <button
      {...buttonProps}
      type={type}
      className={`
        rounded-xl
        font-semibold
        transition-colors
        duration-300
        disabled:pointer-events-none
        disabled:cursor-not-allowed
        disabled:opacity-50
        ${sizes[size]}
        ${styles[variant]}
        ${className}
      `}
    >
      {children}
    </button>
  );
}
