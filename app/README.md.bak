# 📱 Application Module

This module contains the core application code for the GenAI Medical Assistant, implementing a modular architecture for easy maintenance and extensibility.

## 🏗️ Structure Overview

```
app/
├── __init__.py           # Package initialization
├── app.py               # Flask web application entry point
├── components/          # Core ML and data processing components
├── config/             # Configuration management
├── common/             # Shared utilities and helpers
├── templates/          # HTML templates for web interface
└── static/            # Static assets (CSS, JS, images)
```

## 🔧 Components

### `app.py` - Web Application
The main Flask application that provides:
- **Chat Interface**: RESTful endpoints for the medical chat
- **Session Management**: Maintains conversation context
- **Error Handling**: User-friendly error pages and messages
- **Template Rendering**: Serves the web interface

#### Key Routes:
- `GET/POST /`: Main chat interface
- `GET /clear`: Clear conversation history

#### Features:
- Jinja2 template filters for message formatting
- Session-based conversation history
- Comprehensive error handling with user-friendly messages

### `components/` - Core ML Components
Contains the main machine learning and data processing logic:

#### `embeddings.py`
- Multi-fallback embedding model management
- Automatic model selection and error recovery
- Support for multiple HuggingFace embedding models
- CPU-optimized configurations

#### `llm.py`
- Language model loading and management
- Multiple model fallback support
- HuggingFace integration
- Configurable temperature and token limits

#### `pdf_loader.py`
- PDF document processing
- Text chunking with overlap
- Directory-based batch processing
- Recursive text splitting for optimal chunk sizes

#### `retriever.py`
- RAG (Retrieval-Augmented Generation) implementation
- Custom prompt templates for medical queries
- Vector similarity search integration
- Document chain creation and management

#### `vector_store.py`
- FAISS vector database operations
- Vector store creation and loading
- Embedding model integration
- Persistent storage management

### `config/` - Configuration Management

#### `config.py`
Centralized configuration including:
- HuggingFace model settings
- Vector store paths
- Text processing parameters
- Environment variable management

### `common/` - Shared Utilities

#### `logger.py`
- Centralized logging configuration
- File-based logging with rotation
- Multiple log levels
- Structured logging format

#### `custom_exception.py`
- Custom exception classes
- Enhanced error messaging
- Error context preservation
- Debugging information

### `templates/` - Web Interface

#### `index.html`
Modern, responsive chat interface featuring:
- **Real-time Chat**: Instant message display
- **Modern Design**: Professional medical theme
- **Responsive Layout**: Mobile and desktop optimized
- **Loading States**: Visual feedback during processing
- **Error Handling**: User-friendly error display
- **Session Management**: Clear conversation functionality

## 🔄 Data Flow

### 1. Document Processing
```
PDF Files → Text Extraction → Chunking → Embeddings → Vector Store
```

### 2. Query Processing
```
User Query → Embedding → Similarity Search → Context Retrieval → LLM Response
```

### 3. Web Interface Flow
```
User Input → Flask Route → RAG Chain → Response → Template Rendering → User Display
```

## 🛠️ Key Features

### Robust Error Handling
- Multiple fallback models for reliability
- Graceful degradation when models fail
- User-friendly error messages
- Comprehensive logging for debugging

### Performance Optimization
- Efficient vector similarity search
- Optimized text chunking
- CPU-optimized model configurations
- Session-based caching

### Scalability
- Modular component architecture
- Configurable model parameters
- Environment-based configuration
- Stateless request handling

## 🔧 Configuration Options

### Embedding Models (Priority Order)
1. `sentence-transformers/all-MiniLM-L6-v2`
2. `sentence-transformers/all-mpnet-base-v2` 
3. `sentence-transformers/paraphrase-MiniLM-L6-v2`
4. Local cached models

### Language Models (Priority Order)
1. User-configured model (config.py)
2. `gpt2` (reliable fallback)
3. `distilgpt2` (lightweight option)
4. `microsoft/DialoGPT-small` (conversational)

### Text Processing
- **Chunk Size**: 500 characters (configurable)
- **Chunk Overlap**: 50 characters (configurable)
- **Similarity Search**: Top 3 relevant chunks
- **Response Length**: Max 256 tokens

## 🧪 Testing Components

Each component can be tested independently:

```python
# Test embeddings
from app.components.embeddings import get_embedding_model
model = get_embedding_model()

# Test LLM
from app.components.llm import load_llm
llm = load_llm()

# Test vector store
from app.components.vector_store import load_vector_store
db = load_vector_store()

# Test PDF processing
from app.components.pdf_loader import load_pdf_files
docs = load_pdf_files()
```

## 🔍 Monitoring and Debugging

### Logging
- Application logs: `logs/log_YYYY-MM-DD.log`
- Component-specific logging for each module
- Error tracking with stack traces
- Performance metrics logging

### Health Checks
- Model loading verification
- Vector store connectivity
- HuggingFace API authentication
- PDF processing capabilities

## 🚀 Development Guidelines

### Adding New Components
1. Create module in appropriate subdirectory
2. Follow existing error handling patterns
3. Add comprehensive logging
4. Include fallback mechanisms
5. Update configuration as needed

### Code Style
- Follow PEP 8 conventions
- Use type hints where applicable
- Include docstrings for all functions
- Implement proper error handling
- Add unit tests for new functionality

### Performance Considerations
- Use appropriate batch sizes for embeddings
- Implement caching where beneficial
- Monitor memory usage for large documents
- Optimize vector store operations

---

This modular architecture ensures maintainability, scalability, and reliability of the medical assistant application while providing clear separation of concerns and easy extensibility.
