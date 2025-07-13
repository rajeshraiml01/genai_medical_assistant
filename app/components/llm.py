from langchain_huggingface import HuggingFaceEndpoint
from app.config.config import HF_TOKEN, HUGGINGFACE_REPO_ID
import os

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(huggingface_repo_id: str = HUGGINGFACE_REPO_ID, hf_token: str = HF_TOKEN):
    """
    Load LLM with multiple fallback options
    """
    # List of models to try in order of preference
    models_to_try = [
        huggingface_repo_id,  # User specified model
        "gpt2",  # Reliable fallback
        "distilgpt2",  # Smaller alternative
        "microsoft/DialoGPT-small"  # Conversational model
    ]
    
    for model_id in models_to_try:
        try:
            logger.info(f"Attempting to load LLM: {model_id}")
            
            # Set the token as environment variable if provided
            if hf_token:
                os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

            llm = HuggingFaceEndpoint(
                repo_id=model_id,
                temperature=0.3,
                max_new_tokens=256,
                return_full_text=False,
            )

            logger.info(f"LLM loaded successfully: {model_id}")
            return llm
            
        except Exception as e:
            logger.warning(f"Failed to load {model_id}: {e}")
            continue
    
    # If all models fail, raise exception
    error_message = CustomException("Failed to load any LLM model. All fallback options failed.")
    logger.error(str(error_message))
    raise error_message