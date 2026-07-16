# IA-GEN — Roadmap de Desarrollo

> **"La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible."**

---

# Estado del proyecto

**Proyecto:** IA-GEN

**Versión actual:** **v0.4.0**

**Estado:** 🟢 Desarrollo activo

IA-GEN es una plataforma educativa impulsada por Inteligencia Artificial cuyo objetivo es enseñar programación, IA y tecnologías cloud mediante proyectos reales.

Este roadmap representa el plan oficial de desarrollo del proyecto y servirá como referencia para conocer el estado actual del software, las funcionalidades implementadas y las siguientes fases de desarrollo.

---

# Objetivo del proyecto

Construir una plataforma Full Stack moderna que permita a estudiantes aprender Inteligencia Artificial mediante una experiencia completamente práctica.

La plataforma estará compuesta por:

* Frontend moderno con Next.js.
* Backend REST desarrollado con FastAPI.
* Sistema RAG basado en Gemini.
* Base de datos PostgreSQL.
* Base de datos vectorial ChromaDB.
* Despliegue profesional en Oracle Cloud Infrastructure.

---

# Estado general

| Módulo               | Estado           |
| -------------------- | ---------------- |
| Documentación        | ✅ Completado     |
| Arquitectura         | ✅ Completado     |
| Backend Base         | ✅ Completado     |
| Motor IA             | ✅ Completado     |
| Sistema RAG          | ✅ Completado     |
| Ingestión automática | ✅ Completado     |
| API REST             | 🟡 En desarrollo |
| Frontend             | ⏳ Pendiente      |
| PostgreSQL           | ⏳ Pendiente      |
| Autenticación        | ⏳ Pendiente      |
| Docker               | ⏳ Pendiente      |
| Oracle Cloud         | ⏳ Pendiente      |

---

# Historial de versiones

## v0.1.0 — Fundación del proyecto ✅

Objetivo:

Construir la base del proyecto.

Completado:

* Configuración del entorno.
* Python.
* Node.js.
* Visual Studio Code.
* Git.
* GitHub.
* Repositorio inicial.
* Documentación principal.

---

## v0.2.0 — Arquitectura Backend ✅

Objetivo:

Crear la estructura profesional del backend.

Completado:

* Organización de carpetas.
* Configuración del proyecto.
* Sistema de logging.
* Variables de entorno.
* Configuración base.
* Servicios.

---

## v0.3.0 — Motor de Inteligencia Artificial ✅

Objetivo:

Integrar Google Gemini dentro del proyecto.

Completado:

* Gemini Client.
* Embeddings.
* Prompt Builder.
* Chat Service.
* Generación de respuestas.
* Logging de inferencias.

---

## v0.4.0 — Sistema RAG ✅

Objetivo:

Construir el sistema Retrieval-Augmented Generation.

Completado:

### Ingestión

* DocumentLoader.
* Chunking.
* Embeddings.
* IngestionPipeline.
* IngestionService.

### Base vectorial

* ChromaDB.
* VectorStore.
* Retriever.

### Automatización

* Hash SHA-256 de documentos.
* IDs determinísticos para chunks.
* Evitar documentos duplicados.
* Detección de cambios.
* Reindexación automática.
* Actualización inteligente del índice.

### Prompts

* Prompt Builder.
* Contexto dinámico.
* Integración completa con Gemini.

Resultado:

El asistente IA puede responder preguntas utilizando información almacenada en la base vectorial.

---

# Próxima versión

## v0.5.0 — API REST (En desarrollo)

Objetivo:

Exponer todas las funcionalidades mediante FastAPI.

Incluye:

* Endpoint raíz.
* Endpoint Health.
* Endpoint Chat.
* Endpoint Ingest.
* Endpoint Documents.
* Modelos Pydantic.
* Organización por routers.
* Swagger.
* Manejo profesional de errores.

---

# Próximas versiones

## v0.6.0 — Frontend

Tecnologías:

* Next.js
* TypeScript
* Tailwind CSS

Objetivos:

* Landing Page.
* Página de cursos.
* Chat IA.
* Dashboard.
* Navegación.
* Diseño responsive.

---

## v0.7.0 — Usuarios y Autenticación

Objetivos:

* Registro.
* Inicio de sesión.
* JWT.
* Roles.
* Perfil del estudiante.

---

## v0.8.0 — PostgreSQL

Objetivos:

* Usuarios.
* Cursos.
* Conversaciones.
* Historial.
* Persistencia.

---

## v0.9.0 — Infraestructura

Objetivos:

* Docker Backend.
* Docker Frontend.
* Docker Compose.
* Variables de entorno.
* Producción.

---

## v1.0.0 — Primera versión estable

Objetivos:

* Oracle Cloud Infrastructure.
* HTTPS.
* Dominio.
* CI/CD.
* Producción.
* Documentación completa.

---

# Tecnologías

## Frontend

* Next.js
* TypeScript
* Tailwind CSS

## Backend

* Python
* FastAPI

## Inteligencia Artificial

* Google Gemini
* LangChain

## Bases de datos

* PostgreSQL
* ChromaDB

## DevOps

* Docker
* Git
* GitHub
* Oracle Cloud Infrastructure

---

# Filosofía de desarrollo

IA-GEN se desarrolla siguiendo principios de ingeniería de software profesional.

Cada módulo debe cumplir los siguientes criterios antes de considerarse terminado:

* Código limpio.
* Arquitectura desacoplada.
* Documentación actualizada.
* Pruebas funcionales.
* Logging profesional.
* Escalabilidad.
* Mantenibilidad.

---

# Próximo objetivo

**Versión v0.5.0 — API REST**

La siguiente etapa consiste en convertir el motor RAG desarrollado en una API REST profesional utilizando FastAPI para que posteriormente pueda ser consumida por el frontend desarrollado en Next.js.
