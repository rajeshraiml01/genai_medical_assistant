from langchain_community.vectorstores import FAISS
import os

from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vectore_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing FAISS vector store")
            vector_store = FAISS.load_local(DB_FAISS_PATH, 
                                            embedding_model,
                                              allow_dangerous_deserialization=True)
        else:
            logger.info("Creating new FAISS vector store")
            vector_store = FAISS.from_embeddings(embedding_model)
        return vector_store
    except Exception as e:
        error_message = CustomException("Failed to load vector store")
        logger.error(str(error_message))
        return None

# creating new vectorstore function 

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks provided")        
        logger.info("Generating your new vectorstore")
        embedding_model = get_embedding_model()
        db = FAISS.from_documents(text_chunks, embedding_model)
        logger.info("Successfully generated FAISS vector store")
        db.save_local(DB_FAISS_PATH)
        logger.info("Successfully saved FAISS vector store")
        return db
            
    except Exception as e:
        error_message = CustomException("Failed to save vector store")
        logger.error(str(error_message))