# IA-GEN — Roadmap de Desarrollo

> **"La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible."**

---

# Estado del proyecto

**Proyecto:** IA-GEN

**Versión actual:** **v0.6.0**

**Estado:** 🟢 Desarrollo activo

IA-GEN es una plataforma educativa impulsada por Inteligencia Artificial cuyo objetivo es enseñar programación, IA y tecnologías cloud mediante proyectos reales.

Este roadmap representa el plan oficial de desarrollo del proyecto y sirve como referencia para conocer el estado actual del software, las funcionalidades implementadas y las siguientes fases del desarrollo.

---

# Objetivo del proyecto

Construir una plataforma Full Stack moderna que permita a estudiantes aprender Inteligencia Artificial mediante una experiencia completamente práctica.

La plataforma estará compuesta por:

- Frontend moderno con Next.js
- Backend REST desarrollado con FastAPI
- Sistema RAG basado en Gemini
- Base de datos PostgreSQL
- Base de datos vectorial ChromaDB
- Despliegue profesional en Oracle Cloud Infrastructure

---

# Estado general

| Módulo               | Estado        |
| -------------------- | ------------- |
| Documentación        | ✅ Completado |
| Arquitectura         | ✅ Completado |
| Backend Base         | ✅ Completado |
| Motor IA             | ✅ Completado |
| Sistema RAG          | ✅ Completado |
| Ingestión automática | ✅ Completado |
| API REST             | ✅ Completado |
| Frontend             | ✅ Completado |
| PostgreSQL           | ⏳ Pendiente  |
| Autenticación        | ⏳ Pendiente  |
| Docker               | ⏳ Pendiente  |
| Oracle Cloud         | ⏳ Pendiente  |

---

# Historial de versiones

---

## v0.1.0 — Fundación del proyecto ✅

### Objetivo

Construir la base del proyecto.

### Completado

- Configuración del entorno.
- Python.
- Node.js.
- Visual Studio Code.
- Git.
- GitHub.
- Repositorio inicial.
- Documentación principal.

---

## v0.2.0 — Arquitectura Backend ✅

### Objetivo

Crear la estructura profesional del backend.

### Completado

- Organización de carpetas.
- Configuración del proyecto.
- Sistema de logging.
- Variables de entorno.
- Configuración base.
- Arquitectura desacoplada.
- Capa de servicios.

---

## v0.3.0 — Motor de Inteligencia Artificial ✅

### Objetivo

Integrar Google Gemini dentro del proyecto.

### Completado

- Cliente oficial de Gemini.
- Sistema de embeddings.
- Prompt Builder.
- Chat Service.
- Generación de respuestas.
- Logging de inferencias.
- Configuración desacoplada del modelo.

---

## v0.4.0 — Sistema RAG ✅

### Objetivo

Construir el sistema Retrieval-Augmented Generation.

### Ingestión

- DocumentLoader.
- Chunking inteligente.
- Embeddings automáticos.
- IngestionPipeline.
- IngestionService.

### Base vectorial

- ChromaDB.
- VectorStore.
- Retriever.

### Automatización

- Hash SHA-256 de documentos.
- IDs determinísticos para chunks.
- Prevención de documentos duplicados.
- Detección automática de cambios.
- Reindexación inteligente.
- Actualización incremental del índice.

### Prompts

- Prompt Builder.
- Contexto dinámico.
- Integración completa con Gemini.

### Resultado

El asistente IA ya puede responder preguntas utilizando información almacenada en la base vectorial mediante Retrieval-Augmented Generation (RAG).

---

## v0.5.1 — API REST Profesional ✅

### Objetivo

Exponer todas las capacidades del sistema RAG mediante una API REST desarrollada con FastAPI.

### Infraestructura

- FastAPI configurado.
- Arquitectura basada en routers.
- Dependency Injection.
- Configuración desacoplada.
- Variables de entorno.
- Sistema profesional de logging.
- Manejo de excepciones.
- Swagger UI.
- OpenAPI.

### Modelos Pydantic

#### Chat

- ChatRequest.
- ChatResponse.

#### Ingestión

- IngestionRequest.
- IngestionResponse.

#### Documentos

- DocumentsResponse.
- DocumentInfoResponse.

### Endpoints implementados

#### Sistema

- GET /
- GET /health

#### Chat IA

- POST /api/chat

#### Ingestión

- POST /api/ingest

#### Administración de documentos

- GET /api/documents
- GET /api/documents/{filename}

### Integraciones completadas

- FastAPI.
- Gemini.
- ChromaDB.
- Retriever.
- Prompt Builder.
- ChatService.
- IngestionService.
- VectorStore.

### Resultado

IA-GEN dispone de una API REST completamente funcional para interactuar con el sistema RAG, administrar documentos y consultar información desde aplicaciones externas.

---

## v0.6.0 — Frontend IA-GEN ✅

### Objetivo

Construir una interfaz moderna, responsive y escalable utilizando Next.js, TypeScript y Tailwind CSS para servir como base visual de toda la plataforma IA-GEN.

### Tecnologías

- Next.js (App Router)
- TypeScript
- Tailwind CSS

### Arquitectura

- Organización modular de componentes.
- Separación por dominios (`hero`, `courses`, `features`, `about`, `contact`, `footer`, `layout`, `ui`).
- Sistema de componentes reutilizables.
- Arquitectura preparada para consumir APIs REST.
- Sistema de datos desacoplado mediante la carpeta `data/`.

### Landing Page

- Hero principal.
- Hero Illustration.
- Navbar responsive.
- Menú móvil.
- Sección de cursos.
- Sección "¿Por qué IA-GEN?".
- Sección "Sobre IA-GEN".
- Call To Action.
- Footer completo.

### Sistema de componentes

- Button reutilizable.
- Badge.
- FloatingCard.
- CourseCard.
- FeatureCard.
- StatCard.
- Logo.
- HamburgerButton.
- MobileMenu.

### Responsive

- Diseño adaptado para móvil, tablet y escritorio.
- Navbar responsive.
- Hero responsive.
- Ilustración adaptativa.
- Grid responsive en todas las secciones.
- Footer responsive.
- Eliminación de solapamientos visuales.
- Ajustes de tipografía y espaciados para pantallas pequeñas.

### Calidad del código

- Componentes reutilizables.
- Eliminación de código duplicado.
- Renderizado mediante `map()`.
- Separación entre datos y presentación.
- Arquitectura preparada para integración con FastAPI.

### Resultado

IA-GEN dispone ahora de un Frontend completamente funcional, responsive y preparado para integrarse con toda la infraestructura Backend desarrollada previamente.

---

# Próximas versiones

---

## v0.7.0 — Integración Frontend + Backend 🚧

### Objetivo

Conectar toda la interfaz desarrollada en Next.js con la API REST creada en FastAPI para convertir IA-GEN en una plataforma completamente funcional.

### Integración de APIs

- Consumir la API REST desde Next.js.
- Cliente HTTP centralizado.
- Manejo global de errores.
- Variables de entorno para Frontend.
- Configuración por entornos.

### Chat IA

- Integrar el chatbot dentro de la Landing Page.
- Conectar el formulario del chat con `/api/chat`.
- Mostrar respuestas generadas por Gemini.
- Indicador de carga.
- Manejo de errores de conexión.
- Historial de conversación durante la sesión.
- Auto-scroll del chat.

### Cursos

- Obtener cursos desde la API.
- Sustituir datos estáticos por datos dinámicos.
- Preparar la interfaz para futuras ampliaciones.

### Estadísticas

- Consumir estadísticas desde el backend.
- Actualización automática de indicadores.

### Documentación

- Documentar la integración Frontend ↔ Backend.

### Resultado esperado

El usuario podrá conversar con el asistente IA directamente desde la web utilizando el sistema RAG desarrollado durante las fases anteriores.

---

## v0.8.0 — Base de datos y autenticación

### Objetivo

Persistir la información del sistema y permitir que cada usuario tenga su propio espacio dentro de IA-GEN.

### PostgreSQL

- Configuración de PostgreSQL.
- SQLAlchemy.
- Alembic.
- Migraciones.
- Modelado de entidades.

### Usuarios

- Registro.
- Inicio de sesión.
- Recuperación de contraseña.
- Perfil del usuario.

### Autenticación

- JWT.
- Refresh Tokens.
- Protección de rutas.
- Middleware de autenticación.

### Chat

- Guardado del historial de conversaciones.
- Conversaciones por usuario.
- Recuperación del historial.

### Cursos

- Progreso del estudiante.
- Cursos iniciados.
- Cursos completados.

### Resultado esperado

Cada estudiante dispondrá de una cuenta propia con su progreso y su historial de conversaciones almacenados de forma permanente.

---

## v0.9.0 — Plataforma educativa

### Objetivo

Transformar IA-GEN en una plataforma completa de aprendizaje.

### Panel del estudiante

- Dashboard.
- Progreso.
- Cursos activos.
- Historial IA.
- Perfil.

### Cursos

- Sistema de módulos.
- Lecciones.
- Recursos descargables.
- Ejercicios.
- Evaluaciones.

### Inteligencia Artificial

- Tutor personalizado.
- Explicaciones dinámicas.
- Recomendación de contenidos.
- Seguimiento del aprendizaje.

### Administración

- Panel administrativo.
- Gestión de cursos.
- Gestión de documentos RAG.
- Gestión de usuarios.

### Resultado esperado

IA-GEN funcionará como una plataforma educativa completa impulsada por Inteligencia Artificial.

---

## v1.0.0 — Despliegue profesional

### Objetivo

Publicar IA-GEN en producción utilizando Oracle Cloud Infrastructure.

### Infraestructura

- Docker.
- Docker Compose.
- Reverse Proxy.
- HTTPS.
- Certificados SSL.

### Oracle Cloud

- Máquina virtual.
- Despliegue automático.
- Variables de entorno.
- Firewall.
- Monitorización.

### Optimización

- Caché.
- Compresión.
- Optimización de consultas.
- Optimización de imágenes.
- Mejoras de rendimiento.

### Calidad

- Testing.
- Documentación final.
- Revisión completa del proyecto.

### Resultado esperado

## Publicación oficial de IA-GEN como plataforma Full Stack basada en Inteligencia Artificial.

# Estado actual del desarrollo

## ✅ Completado

### Documentación

- README profesional.
- Arquitectura del proyecto.
- Roadmap actualizado.
- Organización de fases.
- Decisiones técnicas documentadas.

### Backend

- FastAPI.
- API REST.
- Google Gemini.
- Sistema RAG.
- Ingestión automática.
- ChromaDB.
- Embeddings.
- Prompt Builder.
- Sistema de logging.
- Arquitectura desacoplada.

### Frontend

- Landing Page completa.
- Navbar responsive.
- Hero responsive.
- Hero Illustration.
- Sección de cursos.
- Sección de características.
- Sección "Sobre IA-GEN".
- Call To Action.
- Footer.
- Componentes reutilizables.
- Sistema de datos desacoplado.
- Responsive para móvil, tablet y escritorio.

---

## 🚧 En desarrollo

Actualmente IA-GEN entra en su siguiente gran etapa:

### Integración Frontend + Backend

Durante esta fase se conectará toda la interfaz desarrollada en Next.js con la API REST creada en FastAPI.

El objetivo es que el usuario pueda interactuar con el asistente inteligente directamente desde la página web utilizando el sistema RAG construido durante las fases anteriores.

---

## 📅 Próximo gran objetivo

Convertir IA-GEN en una aplicación Full Stack completamente funcional.

Las siguientes metas son:

- Integración del chatbot IA.
- Consumo de APIs desde el Frontend.
- Persistencia con PostgreSQL.
- Autenticación mediante JWT.
- Panel del estudiante.
- Despliegue en Oracle Cloud Infrastructure.

---

# Filosofía del proyecto

IA-GEN no pretende ser únicamente una plataforma para realizar consultas a un modelo de Inteligencia Artificial.

Su objetivo es convertirse en un entorno donde cualquier estudiante pueda:

- aprender programación;
- aprender Inteligencia Artificial;
- construir proyectos reales;
- desarrollar un portafolio profesional;
- prepararse para el mercado laboral utilizando tecnologías modernas.

Cada decisión técnica tomada durante el desarrollo sigue una filosofía clara:

> Construir una aplicación escalable, mantenible y preparada para evolucionar sin necesidad de rehacer su arquitectura.

---

# Objetivo final

La versión **v1.0.0** representará el lanzamiento oficial de IA-GEN como plataforma educativa impulsada por Inteligencia Artificial.

El proyecto incluirá:

- Frontend moderno con Next.js.
- Backend profesional con FastAPI.
- Sistema RAG basado en Gemini.
- PostgreSQL.
- ChromaDB.
- Autenticación de usuarios.
- Panel del estudiante.
- Cursos dinámicos.
- Chat inteligente.
- Despliegue en Oracle Cloud Infrastructure.

---

# Estado del proyecto

```text
████████████████████████████████████████

Documentación              ✅ 100%
Arquitectura               ✅ 100%
Backend                    ✅ 100%
Sistema RAG                ✅ 100%
API REST                   ✅ 100%
Frontend                   ✅ 100%

Integración Front + Back   🚧 0%
PostgreSQL                 ⏳
Autenticación              ⏳
Panel del alumno           ⏳
Despliegue OCI             ⏳
```

---

# Próximo hito

🎯 **Frontend v1 finalizado**

El siguiente objetivo consiste en conectar toda la infraestructura Backend desarrollada previamente con la interfaz creada en Next.js para que IA-GEN se convierta en una plataforma completamente funcional.

---

> **"La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible."**

**Proyecto IA-GEN**  
Desarrollado con ❤️ utilizando Next.js, FastAPI, Gemini, ChromaDB y Oracle Cloud.
