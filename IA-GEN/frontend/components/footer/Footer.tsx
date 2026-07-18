import Logo from "../layout/Logo";

export default function Footer() {
  return (
    <footer
      className="
        border-t
        border-cyan-500/20
        bg-slate-950
      "
    >
      <div
        className="
          mx-auto
          grid
          max-w-7xl
          gap-12
          px-6
          py-16
          md:grid-cols-3
        "
      >
        {/* Marca */}

        <div>
          <Logo size="sm" />

          <p className="mt-4 text-slate-400">
            La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible.
          </p>
        </div>

        {/* Navegación */}

        <div>
          <h3 className="font-semibold text-cyan-400">Navegación</h3>

          <ul className="mt-4 space-y-3">
            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Inicio
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Cursos
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Chat IA
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Contacto
            </li>
          </ul>
        </div>

        {/* Tecnologías */}

        <div>
          <h3 className="font-semibold text-cyan-400">Tecnologías</h3>

          <ul className="mt-4 space-y-3">
            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Python
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Gemini AI
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Next.js
            </li>

            <li className="cursor-pointer text-slate-300 transition-colors hover:text-cyan-400">
              Oracle Cloud
            </li>
          </ul>
        </div>
      </div>

      <div
        className="
          border-t
          border-cyan-500/10
          py-6
          text-center
          text-sm
          text-slate-600
        "
      >
        © 2026 IA-GEN · Todos los derechos reservados.
      </div>
    </footer>
  );
}
