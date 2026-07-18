import FeatureCard from "./FeatureCard";
import { features } from "../../data/features";

export default function FeaturesSection() {
  return (
    <section
      className="
        mx-auto
        max-w-7xl
        px-6
        py-24
      "
    >
      <h2 className="text-center text-4xl font-bold text-cyan-400">
        ¿Por qué IA-GEN?
      </h2>

      <p className="mx-auto mt-4 max-w-2xl text-center text-slate-300">
        Una plataforma creada para aprender tecnologías modernas mediante
        proyectos reales y herramientas utilizadas en la industria.
      </p>

      <div
        className="
          mt-16
          grid
          gap-8
          md:grid-cols-2
          xl:grid-cols-4
        "
      >
        {features.map((feature) => (
          <FeatureCard
            key={feature.title}
            emoji={feature.emoji}
            title={feature.title}
            description={feature.description}
          />
        ))}
      </div>
    </section>
  );
}
