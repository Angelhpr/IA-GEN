import type { Metadata, Viewport } from "next";
import { Geist_Mono, Inter } from "next/font/google";

import "./globals.css";

const inter = Inter({
  variable: "--font-geist-sans",
  subsets: ["latin"],
  display: "swap",
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "IA-GEN | Aprende inteligencia artificial",
    template: "%s | IA-GEN",
  },
  description:
    "Proyecto educativo que integra programación, inteligencia artificial, Gemini y recuperación documental mediante una experiencia web interactiva.",
  applicationName: "IA-GEN",
  category: "education",
  keywords: [
    "inteligencia artificial",
    "programación",
    "Gemini",
    "RAG",
    "FastAPI",
    "Next.js",
    "Machine Learning",
    "educación tecnológica",
  ],
  creator: "IA-GEN",
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    type: "website",
    locale: "es",
    siteName: "IA-GEN",
    title: "IA-GEN | Aprende inteligencia artificial",
    description:
      "Explora programación e inteligencia artificial con proyectos prácticos y un asistente conectado a una base documental.",
  },
  twitter: {
    card: "summary",
    title: "IA-GEN | Aprende inteligencia artificial",
    description:
      "Proyecto educativo con Next.js, FastAPI, Gemini y recuperación documental.",
  },
};

export const viewport: Viewport = {
  themeColor: "#0F172A",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="es"
      className={`${inter.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body
        className={`
          flex
          min-h-full
          flex-col
          bg-[#0F172A]
          text-[#F8FAFC]
        `}
      >
        {children}
      </body>
    </html>
  );
}
