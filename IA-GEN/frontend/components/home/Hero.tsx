import HeroIllustration from "./HeroIllustration";
import Button from "../ui/Button";
export default function Hero() {
  return (
    <section className="px-6 py-20 sm:px-8 sm:py-24">
      <div
        className="
          mx-auto
          flex
          max-w-7xl
          flex-col
          items-center
          gap-16
          lg:flex-row
          lg:justify-between
        "
      >
        {/* Columna izquierda */}

        <div className="flex-1 text-center lg:text-left">
          <h1 className="text-5xl font-bold text-cyan-400 sm:text-6xl">
            IA-GEN
          </h1>

          <p className="mt-6 max-w-xl text-lg sm:text-xl">
            Instituto de Inteligencia Artificial para la nueva generación.
          </p>

          <p className="mt-4 max-w-lg italic text-slate-300 text-sm sm:text-base">
            "La IA no llegó a reemplazarte, sino a ayudarte a crear lo
            imposible."
          </p>

          <div
            className="
              mt-10
              flex
              justify-center
              gap-4
              lg:justify-start
            "
          >
            {" "}
            <Button>Comenzar ahora</Button>
            <Button variant="secondary">Explorar cursos</Button>
          </div>
        </div>

        {/* Columna derecha */}

        <div className="flex flex-1 justify-center">
          <HeroIllustration />
        </div>
      </div>
    </section>
  );
}
