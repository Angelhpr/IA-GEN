import StatCard from "./StatCard";
import { stats } from "../../data/about";

export default function AboutSection() {
  return (
    <section
      className="
        mx-auto
        max-w-7xl
        px-6
        py-24
      "
    >
      <div className="grid gap-16 lg:grid-cols-2 lg:items-center">
        {/* Texto */}

        <div>
          <h2 className="text-4xl font-bold text-cyan-400">Sobre IA-GEN</h2>

          <p className="mt-6 text-lg leading-8 text-slate-300">
            IA-GEN nace con el objetivo de enseñar programación, Inteligencia
            Artificial y Cloud Computing mediante una metodología completamente
            práctica basada en proyectos reales.
          </p>

          <p className="mt-6 text-slate-400">
            Queremos que cualquier estudiante pueda construir un portafolio
            profesional mientras aprende las tecnologías que utilizan
            actualmente las empresas.
          </p>
        </div>

        {/* Estadísticas */}

        <div
          className="
            grid
            gap-6
            sm:grid-cols-2
          "
        >
          {stats.map((stat) => (
            <StatCard key={stat.label} value={stat.value} label={stat.label} />
          ))}
        </div>
      </div>
    </section>
  );
}
