from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.vector_store import load_vectore_store
from app.components.llm import load_llm

from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
You are a medical assistant. Answer the following medical questions in 2 - 3 sentences using only the information provided.
in Context: {context}
Question: {question}
Answer:
"""

def set_custom_prompt_template():
    """
    Set a custom prompt template for the RetrievalQA chain.
    """
    try:
        logger.info("Setting custom prompt template for RetrievalQA chain")
        return PromptTemplate(
            input_variables=["context", "question"],
            template=CUSTOM_PROMPT_TEMPLATE
        )
    except Exception as e:
        error_message = CustomException("Failed to set custom prompt template", e)
        logger.error(str(error_message))
        raise error_message

def create_qa_chain():
    """
    Create a RetrievalQA chain with a vector store and LLM.
    """
    try:
        logger.info("Loading vector store...")
        db = load_vectore_store()

        if db is None:
            raise CustomException("Vector store is not loaded properly")
        
        logger.info("Loading LLM...")
        llm = load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, hf_token=HF_TOKEN)

        if llm is None:
            raise CustomException("LLM is not loaded properly")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_type="similarity", search_kwargs={"k": 1}),
            return_source_documents=False,
            chain_type_kwargs={"prompt": set_custom_prompt_template()}
        )
                        
        logger.info("RetrievalQA chain created successfully")
        return qa_chain
    
    except Exception as e:
        error_message = CustomException("Failed to create RetrievalQA chain", e)
        logger.error(str(error_message))
        raise error_message