from langchain_huggingface import HuggingFaceEmbeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import HF_TOKEN
import os

logger = get_logger(__name__)


def get_embedding_model():
    """
    Get embedding model with multiple fallback options
    """
    # Try multiple approaches in order of preference
    approaches = [
        ("huggingface_with_token", _get_hf_with_token),
        ("huggingface_without_token", _get_hf_without_token),
        ("local_cache", _get_local_cached_model),
        ("alternative_model", _get_alternative_model)
    ]
    
    for approach_name, approach_func in approaches:
        try:
            logger.info(f"Attempting {approach_name} approach...")
            model = approach_func()
            logger.info(f"Successfully loaded embedding model using {approach_name}")
            return model
        except Exception as e:
            logger.warning(f"{approach_name} failed: {e}")
            continue
    
    # If all approaches fail, raise the last exception
    raise CustomException("All embedding model approaches failed. Please check your internet connection and HuggingFace token.")


def _get_hf_with_token():
    """Try to get HuggingFace model with authentication token."""
    if not HF_TOKEN:
        raise Exception("No HuggingFace token available")
    
    # Set the token as an environment variable
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN
    
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return model


def _get_hf_without_token():
    """Try to get HuggingFace model without authentication."""
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return model


def _get_local_cached_model():
    """Try to use a locally cached model."""
    # Check if model is already cached locally
    from sentence_transformers import SentenceTransformer
    import tempfile
    
    cache_dir = os.path.join(tempfile.gettempdir(), "sentence_transformers_cache")
    
    if os.path.exists(cache_dir):
        model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True},
            cache_folder=cache_dir
        )
        return model
    else:
        raise Exception("No local cache found")


def _get_alternative_model():
    """Try to use an alternative model that might not require authentication."""
    # Try a smaller, more accessible model
    alternative_models = [
        "sentence-transformers/paraphrase-MiniLM-L3-v2",
        "sentence-transformers/all-mpnet-base-v2"
    ]
    
    for model_name in alternative_models:
        try:
            model = HuggingFaceEmbeddings(
                model_name=model_name,
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
            return model
        except Exception:
            continue
    
    raise Exception("No alternative models accessible")
