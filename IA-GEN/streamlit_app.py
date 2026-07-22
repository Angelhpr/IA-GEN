import logging
import os
import sys
import tempfile
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv


st.set_page_config(
    page_title="IA-GEN",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)


PROJECT_ROOT = Path(__file__).resolve().parent
BACKEND_ROOT = PROJECT_ROOT / "backend"

if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

load_dotenv(
    BACKEND_ROOT / ".env",
    override=False,
)


configured_vector_path = os.getenv("VECTOR_DB_PATH")

if configured_vector_path:
    vector_db_path = Path(configured_vector_path).expanduser()

    if not vector_db_path.is_absolute():
        vector_db_path = BACKEND_ROOT / vector_db_path
else:
    vector_db_path = (
        Path(tempfile.gettempdir())
        / "ia-gen"
        / "vector_db"
    )

os.environ["VECTOR_DB_PATH"] = str(
    vector_db_path.resolve()
)


logger = logging.getLogger("ia_gen_streamlit")


try:
    from app.core.config import settings
    from app.core.exceptions import (
        AIServiceUnavailableError,
        IngestionSourceUnavailableError,
    )
    from app.services.chat_service import ChatService
    from app.services.ingestion_service import IngestionService
except Exception:
    logger.exception(
        "No fue posible importar los servicios de IA-GEN."
    )

    st.error(
        "No fue posible iniciar la aplicación."
    )
    st.info(
        "Configura APP_NAME, APP_VERSION, GEMINI_API_KEY "
        "y MODEL_NAME en los secretos de Streamlit."
    )
    st.stop()


DEFAULT_GREETING = (
    "¡Hola! Soy el asistente del Instituto IA-GEN. "
    "Puedes preguntarme sobre la información disponible "
    "en la base documental."
)


@st.cache_resource(show_spinner=False)
def initialize_knowledge_base() -> tuple[str, ...]:
    ingestion_service = IngestionService(
        source_path=settings.resolved_ingestion_source_path
    )

    ingestion_service.ingest_configured_source()

    return tuple(
        ingestion_service.list_documents()
    )


def get_chat_service() -> ChatService:
    if "chat_service" not in st.session_state:
        st.session_state.chat_service = ChatService()

    return st.session_state.chat_service


def reset_conversation() -> None:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": DEFAULT_GREETING,
        }
    ]


try:
    with st.spinner(
        "Preparando la base de conocimiento..."
    ):
        documents = initialize_knowledge_base()
except IngestionSourceUnavailableError as exc:
    logger.exception(
        "La fuente documental no está disponible."
    )
    st.error(str(exc))
    st.stop()
except Exception:
    logger.exception(
        "No fue posible inicializar la base documental."
    )
    st.error(
        "No fue posible preparar la base documental. "
        "Revisa la configuración y los registros "
        "de la aplicación."
    )
    st.stop()


if "messages" not in st.session_state:
    reset_conversation()


with st.sidebar:
    st.header("Base documental")

    if documents:
        st.success(
            f"{len(documents)} documento(s) disponible(s)"
        )

        for filename in documents:
            st.write(f"- {filename}")
    else:
        st.warning(
            "No hay documentos indexados."
        )

    st.divider()

    if st.button(
        "Limpiar conversación",
        use_container_width=True,
    ):
        reset_conversation()
        st.rerun()

    st.caption(
        f"{settings.APP_NAME} | v{settings.APP_VERSION}"
    )


st.title("IA-GEN")
st.caption(
    "Asistente educativo basado en Gemini y "
    "recuperación de información documental."
)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input(
    "Escribe tu pregunta...",
    max_chars=5000,
    disabled=not bool(documents),
)


if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner(
            "Consultando la base documental..."
        ):
            try:
                result = get_chat_service().chat(prompt)
                answer = result["response"]
            except AIServiceUnavailableError as exc:
                logger.warning(
                    "Servicio de IA no disponible. code=%s",
                    exc.code,
                )
                answer = str(exc)
            except Exception:
                logger.exception(
                    "Error no controlado durante el chat."
                )
                answer = (
                    "No fue posible procesar la pregunta "
                    "en este momento. Intenta nuevamente."
                )

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
