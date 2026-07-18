import Badge from "../ui/Badge";
import FloatingCard from "../ui/FloatingCard";
export default function HeroIllustration() {
  return (
    <div
      className="
        relative
        w-full
        max-w-md
        overflow-hidden
        flex
        items-center
        justify-center
        rounded-3xl
        border
        border-cyan-500/20
        bg-gradient-to-br
        from-slate-900
        via-slate-800
        to-slate-900
        p-8
        shadow-2xl
        lg:max-w-xl
      "
    >
      <div className="text-center">
        <div
          className="
            mx-auto
            mb-6
            flex
            h-20
            w-20
            items-center
            justify-center
            rounded-full
            bg-cyan-500/10
            border
            border-cyan-400/30
            text-4xl
            sm:h-24
            sm:w-24
            sm:text-5xl
          "
        >
          🤖
        </div>

        <h3 className="text-xl sm:text-2xl font-bold text-cyan-400">IA-GEN</h3>

        <p className="mt-3 max-w-sm text-sm text-slate-300 sm:text-base">
          Aprende programación e Inteligencia Artificial mediante proyectos
          reales.
        </p>

        <div className="mt-8 flex flex-wrap justify-center gap-4">
          <Badge>Python</Badge>

          <Badge>Gemini AI</Badge>

          <Badge>Machine Learning</Badge>

          <Badge>Oracle Cloud</Badge>
        </div>
      </div>

      <div className="hidden md:block">
        <FloatingCard position="top-6 left-6">⚡ IA Generativa</FloatingCard>
      </div>
    </div>
  );
}
