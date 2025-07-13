import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

# Use a reliable and supported model for text generation
HUGGINGFACE_REPO_ID="gpt2"
DB_FAISS_PATH="vectorstore/db_faiss"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50