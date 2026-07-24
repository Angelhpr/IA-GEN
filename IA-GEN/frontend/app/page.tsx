import Navbar from "../components/layout/Navbar";
import Hero from "../components/home/Hero";
import CoursesSection from "../components/courses/CoursesSection";
import FeaturesSection from "../components/features/FeaturesSection";
import AboutSection from "../components/about/AboutSection";
import ChatSection from "../components/chat/ChatSection";
import ContactSection from "../components/contact/ContactSection";
import Footer from "../components/footer/Footer";

export default function Home() {
  return (
    <>
      <a
        href="#contenido-principal"
        className="
          sr-only
          fixed
          left-4
          top-4
          z-100
          rounded-lg
          bg-[#2563EB]
          px-4
          py-3
          text-sm
          font-semibold
          text-white
          focus:not-sr-only
          focus:outline-none
          focus:ring-2
          focus:ring-[#60A5FA]
          focus:ring-offset-2
          focus:ring-offset-[#0F172A]
        "
      >
        Saltar al contenido principal
      </a>

      <Navbar />

      <main
        id="contenido-principal"
        className="
          min-h-screen
          overflow-x-clip
          bg-[#0F172A]
          text-[#F8FAFC]
        "
      >
        <Hero />
        <CoursesSection />
        <FeaturesSection />
        <AboutSection />
        <ChatSection />
        <ContactSection />
      </main>

      <Footer />
    </>
  );
}
