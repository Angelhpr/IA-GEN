import Button from "../ui/Button";

export default function MobileMenu() {
  return (
    <div
      className="
        absolute
        left-0
        top-full
        w-full
        border-t
        border-cyan-500/20
        bg-slate-950
        shadow-2xl
      "
    >
      <nav className="flex flex-col px-6 py-6">
        <a
          href="#"
          className="rounded-lg px-4 py-3 text-slate-300 transition-colors hover:bg-slate-900 hover:text-cyan-400"
        >
          Inicio
        </a>

        <a
          href="#"
          className="rounded-lg px-4 py-3 text-slate-300 transition-colors hover:bg-slate-900 hover:text-cyan-400"
        >
          Cursos
        </a>

        <a
          href="#"
          className="rounded-lg px-4 py-3 text-slate-300 transition-colors hover:bg-slate-900 hover:text-cyan-400"
        >
          Chat IA
        </a>

        <a
          href="#"
          className="rounded-lg px-4 py-3 text-slate-300 transition-colors hover:bg-slate-900 hover:text-cyan-400"
        >
          Contacto
        </a>

        <div className="mt-6">
          <Button>Comenzar</Button>
        </div>
      </nav>
    </div>
  );
}
