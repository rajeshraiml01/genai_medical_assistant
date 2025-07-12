import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data Path doesnt exists")
        logger.info(f"Loading files from {DATA_PATH}")

        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            
            logger.info("No pdfs were found")
        else:
            logger.info(f"Succesfully fetched {len(documents)} documents")

        return documents
    except Exception as e:
        error_message = CustomException("Failed to load PDF's")
        logger.error(str(error_message))
        return []


def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("Documents are not present ")
        logger.info(f"Splitting {len(documents)} documents in chunks")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunk")
        return text_chunks
    except Exception as e:
        error_message = CustomException("Failed to Generate Chunks")
        logger.error(str(error_message))
        return []
