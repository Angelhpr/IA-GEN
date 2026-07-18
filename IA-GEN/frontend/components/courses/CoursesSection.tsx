import CourseCard from "./CourseCard";
import { courses } from "../../data/courses";

export default function CoursesSection() {
  return (
    <section
      className="
        mx-auto
        max-w-7xl
        px-6
        py-24
      "
    >
      <h2 className="text-4xl font-bold text-center text-cyan-400">
        Nuestros cursos
      </h2>

      <p className="mt-4 text-center text-slate-300 max-w-2xl mx-auto">
        Aprende las tecnologías más demandadas mediante una metodología basada
        en proyectos reales.
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
    </section>
  );
}
