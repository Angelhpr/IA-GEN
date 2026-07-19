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
    <main className="min-h-screen bg-slate-950 text-white">
      <Navbar />
      <Hero />
      <CoursesSection />
      <FeaturesSection />
      <AboutSection />
      <ChatSection />
      <ContactSection />
      <Footer />
    </main>
  );
}
