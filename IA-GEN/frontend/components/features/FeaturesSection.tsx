import FeatureCard from "./FeatureCard";
import { features } from "../../data/features";

export default function FeaturesSection() {
  return (
    <section
      aria-labelledby="features-title"
      className="
      bg-[#0F172A]
        px-6
        py-16
        md:py-24
      "
    >
      <div
        id="caracteristicas"
        className="
      mx-auto
      max-w-7xl
    "
      >
        <div
          className="
            mx-auto
            max-w-3xl
            text-center
          "
        >
          <span
            className="
              mb-3
              block
              text-xs
              font-semibold
              uppercase
              tracking-[0.2em]
              text-[#7C3AED]
            "
          >
            Experiencia de aprendizaje
          </span>

          <h2
            id="features-title"
            className="
              text-3xl
              font-bold
              leading-tight
              tracking-tight
              text-white
              md:text-5xl
            "
          >
            ¿Por qué aprender con{" "}
            <span
              className="
                bg-linear-to-r
                from-[#2563EB]
                to-[#7C3AED]
                bg-clip-text
                text-transparent
              "
            >
              IA-GEN?
            </span>
          </h2>

          <p
            className="
              mx-auto
              mt-6
              max-w-2xl
              text-base
              leading-7
              text-[#94A3B8]
              md:text-lg
            "
          >
            Un proyecto educativo creado para explorar programación,
            inteligencia artificial y servicios en la nube mediante herramientas
            actuales y experiencias prácticas.
          </p>
        </div>

        <div
          className="
            mt-14
            grid
            grid-cols-1
            gap-5
            sm:grid-cols-2
            xl:grid-cols-4
          "
        >
          {features.map((feature, index) => (
            <FeatureCard
              key={feature.title}
              emoji={feature.emoji}
              title={feature.title}
              description={feature.description}
              index={index}
            />
          ))}
        </div>

        <div
          className="
            mx-auto
            mt-12
            flex
            max-w-3xl
            flex-wrap
            items-center
            justify-center
            gap-3
            text-xs
            text-[#64748B]
          "
        >
          {["Next.js", "FastAPI", "Gemini", "RAG", "ChromaDB"].map(
            (technology) => (
              <span
                key={technology}
                className="
                  rounded-full
                  border
                  border-white/5
                  bg-white/[0.025]
                  px-4
                  py-2
                "
              >
                {technology}
              </span>
            )
          )}
        </div>
      </div>
    </section>
  );
}
