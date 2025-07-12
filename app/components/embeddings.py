from langchain_huggingface import HuggingFaceEmbeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)


def get_embedding_model():
    try:
        logger.info("Loading HuggingFace embeddings model")
        model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        logger.info("Successfully loaded HuggingFace embeddings model")
        return model
    except Exception as e:
        error_message = CustomException("Failed to load embedding model")
        logger.error(str(error_message))
        return None