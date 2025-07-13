from langchain_community.vectorstores import FAISS
import os

from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing FAISS vector store")
            vector_store = FAISS.load_local(DB_FAISS_PATH, 
                                            embedding_model,
                                            allow_dangerous_deserialization=True)
            return vector_store
        else:
            logger.warning("FAISS vector store does not exist. Please run initialization first.")
            return None
    except Exception as e:
        error_message = CustomException("Failed to load vector store", e)
        logger.error(str(error_message))
        raise error_message

# creating new vectorstore function 

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks provided")        
        logger.info("Generating your new vectorstore")
        
        # Get the embedding model
        embedding_model = get_embedding_model()
        
        # Create the FAISS vector store
        db = FAISS.from_documents(text_chunks, embedding_model)
        logger.info("Successfully generated FAISS vector store")
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(DB_FAISS_PATH), exist_ok=True)
        
        # Save the vector store
        db.save_local(DB_FAISS_PATH)
        logger.info("Successfully saved FAISS vector store")
        return db
            
    except Exception as e:
        error_message = CustomException("Failed to save vector store", e)
        logger.error(str(error_message))
        raise error_message
