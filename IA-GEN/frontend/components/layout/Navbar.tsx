"use client";
import { useState } from "react";
import Logo from "./Logo";
import HamburgerButton from "./HamburgerButton";
import MobileMenu from "./MobileMenu";
import Button from "../ui/Button";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="relative w-full border-b border-slate-800 bg-slate-950">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">
        <Logo size="md" />

        <ul className="hidden items-center gap-8 text-slate-300 md:flex">
          <li>
            <a href="#">Inicio</a>
          </li>

          <li>
            <a href="#">Cursos</a>
          </li>

          <li>
            <a href="#">Chat IA</a>
          </li>

          <li>
            <a href="#">Contacto</a>
          </li>
        </ul>
        <div className="hidden md:block">
          <Button>Comenzar</Button>
        </div>
        <div className="md:hidden">
          <HamburgerButton isOpen={isOpen} onClick={() => setIsOpen(!isOpen)} />
        </div>
      </div>
      {isOpen && <MobileMenu />}
    </nav>
  );
}
