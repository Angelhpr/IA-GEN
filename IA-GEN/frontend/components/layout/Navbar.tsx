"use client";

import { useEffect, useState } from "react";

import HamburgerButton from "./HamburgerButton";
import Logo from "./Logo";
import MobileMenu from "./MobileMenu";

const navigationLinks = [
  {
    label: "Inicio",
    href: "#inicio",
  },
  {
    label: "Cursos",
    href: "#cursos",
  },
  {
    label: "Chat IA",
    href: "#chat-ia",
  },
  {
    label: "Contacto",
    href: "#contacto",
  },
];

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    function handleScroll() {
      setIsScrolled(window.scrollY > 24);
    }

    handleScroll();

    window.addEventListener("scroll", handleScroll, {
      passive: true,
    });

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  function closeMobileMenu() {
    setIsOpen(false);
  }

  return (
    <nav
      aria-label="Navegación principal"
      className={`
        sticky
        top-0
        z-50
        w-full
        border-b
        transition-all
        duration-300
        ${
          isScrolled
            ? `
              border-white/10
              bg-[#0F172A]/95
              shadow-[0_12px_35px_rgba(2,6,23,0.40)]
              backdrop-blur-xl
            `
            : `
              border-white/5
              bg-[#0F172A]/85
              backdrop-blur-lg
            `
        }
      `}
    >
      <div
        className="
          mx-auto
          flex
          h-16
          max-w-7xl
          items-center
          justify-between
          px-6
          lg:px-8
        "
      >
        <a
          href="#inicio"
          aria-label="Ir al inicio de IA-GEN"
          className="
            shrink-0
            rounded-lg
            outline-none
            transition-opacity
            hover:opacity-90
            focus-visible:ring-2
            focus-visible:ring-[#2563EB]
            focus-visible:ring-offset-2
            focus-visible:ring-offset-[#0F172A]
          "
        >
          <Logo size="sm" />
        </a>

        <ul
          className="
            hidden
            items-center
            gap-8
            md:flex
          "
        >
          {navigationLinks.map((link) => (
            <li key={link.href}>
              <a
                href={link.href}
                className="
                  rounded-md
                  px-1
                  py-2
                  text-sm
                  font-medium
                  text-[#94A3B8]
                  outline-none
                  transition-colors
                  duration-200
                  hover:text-white
                  focus-visible:text-white
                  focus-visible:ring-2
                  focus-visible:ring-[#2563EB]
                "
              >
                {link.label}
              </a>
            </li>
          ))}
        </ul>

        <div className="hidden items-center md:flex">
          <a
            href="#chat-ia"
            className="
              rounded-xl
              bg-[#2563EB]
              px-5
              py-2.5
              text-sm
              font-semibold
              text-white
              shadow-[0_8px_24px_rgba(37,99,235,0.20)]
              outline-none
              transition-all
              duration-200
              hover:bg-[#1D4ED8]
              hover:shadow-[0_0_24px_rgba(37,99,235,0.40)]
              focus-visible:ring-2
              focus-visible:ring-[#60A5FA]
              focus-visible:ring-offset-2
              focus-visible:ring-offset-[#0F172A]
            "
          >
            Probar asistente
          </a>
        </div>

        <div className="md:hidden">
          <HamburgerButton
            isOpen={isOpen}
            onClick={() => setIsOpen((currentValue) => !currentValue)}
          />
        </div>
      </div>

      {isOpen && (
        <div onClick={closeMobileMenu}>
          <MobileMenu />
        </div>
      )}
    </nav>
  );
}
