import Button from "../ui/Button";

export default function ContactSection() {
  return (
    <section
      className="
        mx-auto
        max-w-7xl
        px-6
        py-24
      "
    >
      <div
        className="
          rounded-3xl
          border
          border-cyan-500/20
          bg-gradient-to-r
          from-slate-900
          via-slate-800
          to-slate-900
          p-10
          sm:p-16
          text-center
        "
      >
        <h2 className="text-4xl font-bold text-cyan-400">
          Empieza hoy tu camino en IA
        </h2>

        <p className="mx-auto mt-6 max-w-3xl text-lg text-slate-300">
          Aprende programación, Inteligencia Artificial y Cloud Computing
          construyendo proyectos reales desde el primer día.
        </p>

        <div className="mt-10 flex justify-center">
          <Button size="lg">Comenzar ahora</Button>
        </div>
      </div>
    </section>
  );
}
