interface LogoProps {
  size?: "sm" | "md" | "lg";
}

export default function Logo({
  size = "md",
}: LogoProps) {
  const sizes = {
    sm: "text-2xl",
    md: "text-4xl",
    lg: "text-6xl",
  };

  return (
    <h1
      className={`
        ${sizes[size]}
        font-bold
        text-cyan-400
        tracking-wide
      `}
    >
      IA-GEN
    </h1>
  );
}