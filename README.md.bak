# 🏥 GenAI Medical Assistant

A Retrieval-Augmented Generation (RAG) powered medical chatbot that provides intelligent responses to medical queries using HuggingFace models and FAISS vector storage.

## 🌟 Overview

This medical assistant leverages state-of-the-art natural language processing to provide accurate, contextual medical information by:
- Processing medical documents (PDFs) and creating searchable knowledge base
- Using advanced embedding models for semantic similarity search
- Implementing RAG architecture for context-aware responses
- Providing a user-friendly web interface for medical consultations

## 🚀 Features

- **RAG-based Medical Queries**: Ask complex medical questions and get contextual answers
- **PDF Document Processing**: Automatically processes medical literature and documents
- **Vector-based Search**: Uses FAISS for fast similarity search across medical knowledge
- **Modern Web Interface**: Clean, responsive UI for easy interaction
- **Fallback Model Support**: Multiple embedding and LLM model options for reliability
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Session Management**: Maintains conversation context across user sessions

## 🏗️ Architecture

```
genai_medical_assistant/
├── app/                    # Main application code
│   ├── components/         # Core ML components
│   │   ├── embeddings.py   # Embedding model management
│   │   ├── llm.py         # Language model configuration
│   │   ├── pdf_loader.py  # Document processing
│   │   ├── retriever.py   # RAG chain implementation
│   │   └── vector_store.py # FAISS vector store management
│   ├── config/            # Configuration management
│   │   └── config.py      # Application settings
│   ├── common/            # Shared utilities
│   │   ├── logger.py      # Logging configuration
│   │   └── custom_exception.py # Error handling
│   ├── templates/         # HTML templates
│   │   └── index.html     # Main chat interface
│   └── app.py            # Flask web application
├── data/                 # Medical documents storage
├── vectorstore/          # FAISS vector database
├── logs/                 # Application logs
└── debugging/           # Development and testing scripts
```

## 📋 Prerequisites

- Python 3.8+
- HuggingFace account and API token
- Virtual environment (recommended)

## 🛠️ Installation

### 1. Clone and Setup Environment
```bash
# Navigate to project directory
cd genai_medical_assistant

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/MacOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install from setup.py
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project root:
```env
HF_TOKEN="your_huggingface_token_here"
HUGGINGFACEHUB_API_TOKEN="your_huggingface_token_here"
```

**Get your HuggingFace token:**
1. Visit [HuggingFace](https://huggingface.co/)
2. Sign up/Login to your account
3. Go to Settings → Access Tokens
4. Create a new token with write permissions

### 4. Prepare Medical Documents
```bash
# Place your PDF medical documents in the data/ folder
mkdir -p data/
# Copy your medical PDFs to data/ directory
```

### 5. Initialize Vector Store
Before running the application, you need to process your medical documents:

```python
# Create an initialization script or use the Python REPL
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store

# Load and process documents
documents = load_pdf_files()
text_chunks = create_text_chunks(documents)

# Create vector store
vector_store = save_vector_store(text_chunks)
print("Vector store initialized successfully!")
```

## 🚀 Usage

### Starting the Application
```bash
# Activate virtual environment (if not already active)
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/MacOS

# Run the Flask application
python app/app.py
```

The application will be available at `http://localhost:5000`

### Using the Medical Assistant

1. **Open your browser** and navigate to `http://localhost:5000`
2. **Ask medical questions** in the chat interface
3. **Get contextual responses** based on your medical document corpus
4. **Clear conversation** using the "Clear" button when needed

### Example Queries
- "What are the symptoms of diabetes?"
- "Explain the treatment options for hypertension"
- "What are the side effects of aspirin?"
- "How is pneumonia diagnosed?"

## 🔧 Configuration

### Model Configuration (`app/config/config.py`)
```python
# HuggingFace model settings
HUGGINGFACE_REPO_ID = "gpt2"  # Primary LLM model
HF_TOKEN = "your_token"       # HuggingFace API token

# Vector store settings
DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "data/"

# Text processing settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
```

### Embedding Models
The system supports multiple embedding models with automatic fallback:
1. `sentence-transformers/all-MiniLM-L6-v2` (Primary)
2. `sentence-transformers/all-mpnet-base-v2` (Fallback)
3. `sentence-transformers/paraphrase-MiniLM-L6-v2` (Alternative)

### Language Models
Multiple LLM options with automatic fallback:
1. User-specified model (configurable)
2. `gpt2` (Reliable fallback)
3. `distilgpt2` (Lightweight option)
4. `microsoft/DialoGPT-small` (Conversational model)

## 🧪 Testing

### Run Comprehensive Tests
```bash
# Navigate to debugging folder
cd debugging/

# Run complete system test
python test_complete_fix.py
```

### Test Individual Components
```bash
# Test embedding functionality
python debugging/test_embedding_fix.py

# Test HuggingFace authentication
python debugging/setup_huggingface_auth.py
```

## 📊 Project Structure Details

### Core Components

#### `app/components/`
- **`embeddings.py`**: Multi-fallback embedding model management
- **`llm.py`**: Language model loading with fallback options
- **`pdf_loader.py`**: PDF document processing and text chunking
- **`retriever.py`**: RAG chain implementation with custom prompts
- **`vector_store.py`**: FAISS vector database operations

#### `app/common/`
- **`logger.py`**: Centralized logging configuration
- **`custom_exception.py`**: Custom error handling

#### `app/templates/`
- **`index.html`**: Modern, responsive chat interface

### Data Flow
1. **Document Ingestion**: PDFs → Text chunks → Embeddings
2. **Vector Storage**: Embeddings → FAISS database
3. **Query Processing**: User query → Embedding → Similarity search
4. **Response Generation**: Retrieved context + LLM → Response

## 🎨 Web Interface Features

- **Modern Design**: Clean, professional medical interface
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Real-time Chat**: Instant responses with loading indicators
- **Message History**: Persistent conversation within session
- **Error Handling**: User-friendly error messages
- **Clear Session**: Reset conversation functionality

## 🔧 Troubleshooting

### Common Issues

#### 1. Vector Store Not Found
```bash
Error: FAISS vector store does not exist
Solution: Run the vector store initialization script
```

#### 2. HuggingFace Authentication
```bash
Error: Authentication failed
Solution: Check your HF_TOKEN in .env file
```

#### 3. Model Loading Issues
```bash
Error: Failed to load model
Solution: The system will automatically try fallback models
```

#### 4. Memory Issues
```bash
Error: Out of memory
Solution: Reduce CHUNK_SIZE in config.py or use smaller models
```

### Logs and Debugging
- Check `logs/` folder for detailed application logs
- Use debugging scripts in `debugging/` folder
- Enable debug mode in Flask for development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **HuggingFace**: For providing excellent transformer models and embeddings
- **LangChain**: For RAG implementation framework
- **FAISS**: For efficient vector similarity search
- **Flask**: For the web application framework

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the logs in `logs/` folder
- Run the debugging scripts for system health checks

---

**Author**: Rajesh R  
**Version**: 0.1  
**Last Updated**: July 2025