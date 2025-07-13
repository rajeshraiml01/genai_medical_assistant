from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from app.components.vector_store import load_vector_store
from app.components.llm import load_llm

from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
You are a medical assistant. Answer the following medical questions in 2 - 3 sentences using only the information provided.

Context: {context}

Question: {input}

Answer:
"""

def set_custom_prompt_template():
    """
    Set a custom prompt template for the retrieval chain.
    """
    try:
        logger.info("Setting custom prompt template for retrieval chain")
        return ChatPromptTemplate.from_template(CUSTOM_PROMPT_TEMPLATE)
    except Exception as e:
        error_message = CustomException("Failed to set custom prompt template", e)
        logger.error(str(error_message))
        raise error_message

def create_qa_chain():
    """
    Create a retrieval chain with a vector store and LLM.
    """
    try:
        logger.info("Loading vector store...")
        db = load_vector_store()

        if db is None:
            raise CustomException("Vector store is not loaded properly")
        
        logger.info("Loading LLM...")
        llm = load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, hf_token=HF_TOKEN)

        if llm is None:
            raise CustomException("LLM is not loaded properly")
        
        # Create the prompt template
        prompt = set_custom_prompt_template()
        
        # Create document chain
        document_chain = create_stuff_documents_chain(llm, prompt)
        
        # Create retrieval chain
        retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
                        
        logger.info("Retrieval chain created successfully")
        return retrieval_chain
    
    except Exception as e:
        error_message = CustomException("Failed to create retrieval chain", e)
        logger.error(str(error_message))
        raise error_message