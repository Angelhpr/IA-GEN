# IA-GEN — Roadmap de Desarrollo

> **"La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible."**

---

# Estado del proyecto

**Proyecto:** IA-GEN

**Versión actual:** **v0.5.1**

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

| Módulo | Estado |
|---------|--------|
| Documentación | ✅ Completado |
| Arquitectura | ✅ Completado |
| Backend Base | ✅ Completado |
| Motor IA | ✅ Completado |
| Sistema RAG | ✅ Completado |
| Ingestión automática | ✅ Completado |
| API REST | ✅ Completado |
| Frontend | ⏳ Pendiente |
| PostgreSQL | ⏳ Pendiente |
| Autenticación | ⏳ Pendiente |
| Docker | ⏳ Pendiente |
| Oracle Cloud | ⏳ Pendiente |

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

---

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

---

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

---

### Endpoints implementados

#### Sistema

- `GET /`
- `GET /health`

#### Chat IA

- `POST /api/chat`

Permite consultar al asistente utilizando el sistema RAG completo.

---

#### Ingestión

- `POST /api/ingest`

Procesa automáticamente todos los documentos de una carpeta.

Incluye:

- generación de embeddings;
- detección de cambios mediante SHA-256;
- actualización automática del índice;
- prevención de duplicados.

---

#### Administración de documentos

##### `GET /api/documents`

Devuelve todos los documentos actualmente indexados en ChromaDB.

##### `GET /api/documents/{filename}`

Devuelve información detallada de un documento:

- nombre;
- cantidad de chunks;
- hash SHA-256;
- ruta original del documento.

Además incorpora manejo profesional de errores mediante:

- HTTP 404 cuando el documento no existe;
- respuestas tipadas mediante Pydantic.

---

### Integraciones completadas

- FastAPI.
- Gemini.
- ChromaDB.
- Retriever.
- Prompt Builder.
- ChatService.
- IngestionService.
- VectorStore.

---

### Pruebas realizadas

Se verificó correctamente el funcionamiento de:

- Inicio del servidor.
- Swagger UI.
- OpenAPI.
- Endpoint raíz.
- Health Check.
- Chat IA.
- Recuperación de contexto desde ChromaDB.
- Ingestión automática.
- Listado de documentos.
- Consulta individual de documentos.
- Manejo de errores HTTP.
- Logging completo del flujo de ejecución.

---

### Resultado

IA-GEN dispone ahora de una API REST completamente funcional para interactuar con el sistema RAG, administrar documentos y consultar información desde aplicaciones externas.
---

# Próximas versiones

---

## v0.6.0 — Frontend

### Objetivo

Construir la interfaz moderna de IA-GEN utilizando Next.js.

### Tecnologías

- Next.js
- TypeScript
- Tailwind CSS

### Objetivos principales

#### Landing Page

- Página principal.
- Presentación del proyecto.
- Sección de cursos.
- Filosofía IA-GEN.
- Call To Action.

#### Chat IA

- Interfaz moderna.
- Comunicación con `/api/chat`.
- Historial de conversación.
- Indicador de carga.
- Manejo de errores.

#### Navegación

- Navbar.
- Footer.
- Diseño responsive.
- Navegación entre páginas.

#### Dashboard

- Panel inicial.
- Visualización de cursos.
- Acceso al asistente IA.
- Diseño reutilizable.

#### Integración

- Consumo completo de la API REST.
- Manejo de estados.
- Componentes reutilizables.

---

## v0.7.0 — Usuarios y Autenticación

### Objetivo

Agregar autenticación segura y gestión de usuarios.

### Funcionalidades

- Registro.
- Inicio de sesión.
- JWT.
- Refresh Tokens.
- Roles.
- Perfil del estudiante.
- Protección de rutas.
- Persistencia de sesión.

---

## v0.8.0 — PostgreSQL

### Objetivo

Persistir toda la información de la plataforma.

### Entidades

- Usuarios.
- Cursos.
- Conversaciones.
- Historial.
- Progreso.
- Configuración.

### Objetivos

- SQLAlchemy.
- Alembic.
- Migraciones.
- Relaciones.
- Repositorios.
- Servicios desacoplados.

---

## v0.9.0 — Infraestructura

### Objetivo

Preparar IA-GEN para producción.

### DevOps

- Docker Backend.
- Docker Frontend.
- Docker Compose.
- Variables de entorno.
- Configuración de producción.

### Calidad

- Optimización.
- Logs centralizados.
- Configuración segura.
- Preparación para despliegue.

---

## v1.0.0 — Primera versión estable

### Objetivo

Publicar la primera versión oficial de IA-GEN.

### Infraestructura Cloud

- Oracle Cloud Infrastructure.
- HTTPS.
- Dominio propio.
- Despliegue automatizado.
- CI/CD.
- Monitorización.

### Plataforma

- Plataforma completamente funcional.
- Sistema RAG en producción.
- Frontend moderno.
- Backend escalable.
- Base de datos persistente.
- Documentación final.

---

# Arquitectura del proyecto

```
                Frontend (Next.js)
                        │
                        ▼
                FastAPI REST API
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
   ChatService                  IngestionService
        │                               │
        ▼                               ▼
    Retriever                    IngestionPipeline
        │                               │
        └───────────────┬───────────────┘
                        ▼
                   VectorStore
                        │
                   ChromaDB
                        │
                        ▼
               Google Gemini API
```

---

# Tecnologías

## Frontend

- Next.js
- TypeScript
- Tailwind CSS

---

## Backend

- Python
- FastAPI
- Pydantic

---

## Inteligencia Artificial

- Google Gemini
- LangChain

---

## Retrieval-Augmented Generation

- ChromaDB
- Embeddings
- Retriever
- Prompt Builder

---

## Bases de datos

- PostgreSQL
- ChromaDB

---

## DevOps

- Docker
- Git
- GitHub
- Oracle Cloud Infrastructure

---

# Filosofía de desarrollo

IA-GEN se desarrolla siguiendo principios de ingeniería de software profesional.

Cada módulo debe cumplir los siguientes criterios antes de considerarse terminado:

- Código limpio.
- Arquitectura desacoplada.
- Responsabilidad única.
- Documentación actualizada.
- Pruebas funcionales.
- Logging profesional.
- Escalabilidad.
- Mantenibilidad.
- Reutilización.
- Buenas prácticas de desarrollo.

---

# Estado actual del proyecto

Actualmente IA-GEN dispone de:

✅ Arquitectura profesional.

✅ Backend desacoplado.

✅ Integración completa con Google Gemini.

✅ Sistema RAG completamente funcional.

✅ Base vectorial mediante ChromaDB.

✅ Ingestión inteligente de documentos.

✅ API REST completamente documentada.

✅ Swagger UI.

✅ Dependency Injection.

✅ Modelos Pydantic.

✅ Manejo profesional de errores.

El siguiente gran paso será comenzar el desarrollo del Frontend utilizando Next.js para ofrecer una interfaz moderna conectada con toda la infraestructura ya construida.

---

# Próximo objetivo

## v0.6.0 — Frontend Next.js

Los primeros objetivos serán:

- Conectar el Frontend con la API REST.
- Crear la Landing Page.
- Construir la interfaz del chat IA.
- Consumir los endpoints del Backend.
- Crear componentes reutilizables.
- Implementar una interfaz responsive.
- Mantener la arquitectura modular del proyecto.

---

# Visión del proyecto

IA-GEN no pretende ser únicamente un chatbot.

El objetivo es construir una plataforma educativa moderna donde los estudiantes aprendan Inteligencia Artificial desarrollando proyectos reales, utilizando las mismas herramientas que emplea la industria del software.

Cada versión acerca el proyecto a esa visión.

---

> **"La IA no llegó a reemplazarte, sino a ayudarte a crear lo imposible."**

**— Proyecto IA-GEN**