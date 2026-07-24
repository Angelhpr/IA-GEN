import CourseCard from "./CourseCard";
import { courses } from "../../data/courses";

export default function CoursesSection() {
  return (
    <section
      aria-labelledby="courses-title"
      className="
      bg-[#0F172A]
        px-6
        py-16
        md:py-24
      "
    >
      <div
        id="cursos"
        className="
          mx-auto
          max-w-7xl
        "
      >
        <div
          className="
            mb-14
            flex
            flex-col
            gap-6
            md:flex-row
            md:items-end
            md:justify-between
          "
        >
          <div>
            <span
              className="
                mb-3
                block
                text-xs
                font-semibold
                uppercase
                tracking-[0.2em]
                text-[#2563EB]
              "
            >
              Cursos
            </span>

            <h2
              id="courses-title"
              className="
                max-w-2xl
                text-3xl
                font-bold
                leading-tight
                tracking-tight
                text-white
                md:text-5xl
              "
            >
              Aprende las bases para crear soluciones con inteligencia
              artificial.
            </h2>
          </div>

          <p
            className="
              max-w-xl
              text-base
              leading-7
              text-[#94A3B8]
              md:text-right
            "
          >
            Explora tecnologías de programación, inteligencia artificial,
            aprendizaje automático y servicios en la nube mediante proyectos
            prácticos.
          </p>
        </div>

        <div
          className="
            grid
            grid-cols-1
            gap-5
            sm:grid-cols-2
            xl:grid-cols-4
          "
        >
          {courses.map((course) => (
            <CourseCard
              key={course.title}
              emoji={course.emoji}
              title={course.title}
              level={course.level}
              description={course.description}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
