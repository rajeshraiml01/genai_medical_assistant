# 🧩 Components Module

This module contains the core machine learning and data processing components that power the GenAI Medical Assistant's RAG (Retrieval-Augmented Generation) functionality.

## 📁 Module Overview

```
components/
├── __init__.py         # Package initialization
├── embeddings.py       # Embedding model management with fallbacks
├── llm.py             # Language model loading and configuration
├── pdf_loader.py      # PDF document processing and text chunking
├── retriever.py       # RAG chain implementation
└── vector_store.py    # FAISS vector database operations
```

## 🔧 Component Details

### `embeddings.py` - Embedding Model Management

**Purpose**: Handles embedding model loading with multiple fallback strategies for reliability.

#### Key Features:
- **Multi-Strategy Loading**: 4 different approaches to load embedding models
- **Automatic Fallbacks**: If one method fails, automatically tries the next
- **HuggingFace Integration**: Seamless integration with HF models
- **CPU Optimization**: Configured for optimal CPU performance
- **Normalization**: Built-in embedding normalization for better similarity search

#### Available Strategies:
1. **HuggingFace with Token**: Authenticated access to HF models
2. **HuggingFace without Token**: Public model access
3. **Local Cache**: Uses locally cached models
4. **Alternative Models**: Fallback to different model architectures

#### Supported Models:
- `sentence-transformers/all-MiniLM-L6-v2` (Primary - 384 dim)
- `sentence-transformers/all-mpnet-base-v2` (High quality - 768 dim)
- `sentence-transformers/paraphrase-MiniLM-L6-v2` (Alternative - 384 dim)

#### Usage:
```python
from app.components.embeddings import get_embedding_model

# Get embedding model (with automatic fallbacks)
model = get_embedding_model()

# Embed single query
embedding = model.embed_query("What is diabetes?")

# Embed multiple documents
embeddings = model.embed_documents(["doc1", "doc2", "doc3"])
```

---

### `llm.py` - Language Model Management

**Purpose**: Manages language model loading with fallback support for reliable text generation.

#### Key Features:
- **Multiple Model Support**: Configurable primary and fallback models
- **HuggingFace Endpoint**: Uses HF inference endpoints for scalability
- **Token Management**: Automatic API token handling
- **Temperature Control**: Configurable response creativity
- **Token Limiting**: Controlled response length

#### Supported Models:
1. **Primary**: User-configurable (default: `gpt2`)
2. **Fallback 1**: `gpt2` (reliable, general-purpose)
3. **Fallback 2**: `distilgpt2` (lighter, faster)
4. **Fallback 3**: `microsoft/DialoGPT-small` (conversational)

#### Configuration:
```python
# Model parameters
temperature=0.3          # Response creativity (0-1)
max_new_tokens=256      # Maximum response length
return_full_text=False  # Return only new generated text
```

#### Usage:
```python
from app.components.llm import load_llm

# Load LLM with fallbacks
llm = load_llm(
    huggingface_repo_id="gpt2",
    hf_token="your_token"
)

# Generate response
response = llm.invoke("Explain diabetes symptoms")
```

---

### `pdf_loader.py` - Document Processing

**Purpose**: Handles PDF document loading, processing, and text chunking for the knowledge base.

#### Key Features:
- **Directory Processing**: Batch process all PDFs in a directory
- **Individual File Processing**: Process specific PDF files
- **Intelligent Chunking**: Recursive text splitting with overlap
- **Metadata Preservation**: Maintains document source information
- **Error Handling**: Robust error handling for corrupted files

#### Text Chunking Strategy:
- **Chunk Size**: 500 characters (configurable)
- **Overlap**: 50 characters (configurable)
- **Method**: Recursive character text splitter
- **Preserves Context**: Maintains semantic coherence

#### Functions:

##### `load_pdf_files()`
Loads all PDF files from the configured data directory.
```python
documents = load_pdf_files()
# Returns: List[Document] with content and metadata
```

##### `create_text_chunks(documents)`
Splits documents into manageable chunks for embedding.
```python
chunks = create_text_chunks(documents)
# Returns: List[Document] with chunked content
```

##### `load_pdf_data(pdf_file_path)`
Processes a specific PDF file.
```python
chunks = load_pdf_data("path/to/medical_document.pdf")
# Returns: List[Document] with processed chunks
```

---

### `retriever.py` - RAG Chain Implementation

**Purpose**: Implements the Retrieval-Augmented Generation chain for context-aware medical responses.

#### Key Features:
- **Custom Medical Prompts**: Specialized prompt templates for medical queries
- **Context Integration**: Combines retrieved documents with user queries
- **Similarity Search**: Top-k document retrieval based on query similarity
- **Chain Management**: Orchestrates the complete RAG workflow

#### RAG Workflow:
1. **Query Embedding**: Convert user query to vector representation
2. **Similarity Search**: Find top-3 most relevant document chunks
3. **Context Preparation**: Format retrieved documents as context
4. **Prompt Construction**: Combine context with user query
5. **LLM Generation**: Generate contextual response

#### Custom Prompt Template:
```python
CUSTOM_PROMPT_TEMPLATE = """
You are a medical assistant. Answer the following medical questions in 2 - 3 sentences using only the information provided.

Context: {context}

Question: {input}

Answer:
"""
```

#### Functions:

##### `set_custom_prompt_template()`
Creates the medical-specific prompt template.

##### `create_qa_chain()`
Builds the complete RAG chain with vector store and LLM.
```python
qa_chain = create_qa_chain()
response = qa_chain.invoke({"input": "What are diabetes symptoms?"})
```

---

### `vector_store.py` - Vector Database Operations

**Purpose**: Manages FAISS vector database operations for efficient similarity search.

#### Key Features:
- **FAISS Integration**: High-performance vector similarity search
- **Persistent Storage**: Save and load vector databases
- **Embedding Integration**: Seamless connection with embedding models
- **Error Recovery**: Graceful handling of database issues

#### FAISS Configuration:
- **Index Type**: Flat (exact search for accuracy)
- **Distance Metric**: L2 (Euclidean distance)
- **Serialization**: Pickle-based for Python compatibility
- **Safety**: Controlled deserialization for security

#### Functions:

##### `load_vector_store()`
Loads existing vector store from disk.
```python
db = load_vector_store()
if db is None:
    print("Vector store not found - need to initialize")
```

##### `save_vector_store(text_chunks)`
Creates and saves new vector store from text chunks.
```python
# Create from documents
text_chunks = create_text_chunks(documents)
db = save_vector_store(text_chunks)

# Vector store saved to configured path
```

#### Vector Store Structure:
```
vectorstore/db_faiss/
├── index.faiss    # FAISS index file
└── index.pkl      # Metadata and document content
```

---

## 🔄 Component Interactions

### Data Flow Through Components:

1. **Document Ingestion**:
   ```
   PDF Files → pdf_loader.py → Text Chunks
   ```

2. **Vector Store Creation**:
   ```
   Text Chunks → embeddings.py → Vectors → vector_store.py → FAISS DB
   ```

3. **Query Processing**:
   ```
   User Query → embeddings.py → Query Vector → vector_store.py → Similar Docs
   ```

4. **Response Generation**:
   ```
   Similar Docs + Query → retriever.py → llm.py → Final Response
   ```

## 🛠️ Configuration

### Environment Variables:
```env
HF_TOKEN="your_huggingface_token"
HUGGINGFACEHUB_API_TOKEN="your_huggingface_token"
```

### Configuration Parameters:
```python
# From app/config/config.py
HUGGINGFACE_REPO_ID = "gpt2"           # Primary LLM model
DB_FAISS_PATH = "vectorstore/db_faiss"  # Vector store location
DATA_PATH = "data/"                     # PDF documents location
CHUNK_SIZE = 500                        # Text chunk size
CHUNK_OVERLAP = 50                      # Chunk overlap size
```

## 🧪 Testing Components

### Individual Component Testing:
```python
# Test each component independently
from app.components import *

# Test embeddings
model = get_embedding_model()
embedding = model.embed_query("test")

# Test LLM
llm = load_llm()
response = llm.invoke("Hello")

# Test PDF loading
docs = load_pdf_files()
chunks = create_text_chunks(docs)

# Test vector store
db = save_vector_store(chunks)
loaded_db = load_vector_store()

# Test retriever
qa_chain = create_qa_chain()
result = qa_chain.invoke({"input": "test question"})
```

### System Integration Test:
```python
# Full workflow test
from debugging.test_complete_fix import main
success = main()  # Returns True if all tests pass
```

## 🔍 Error Handling

### Common Issues and Solutions:

#### Embedding Model Loading:
- **Issue**: Model download fails
- **Solution**: Automatic fallback to alternative models
- **Fallback Order**: HF with token → HF without token → Local cache → Alternative models

#### LLM Loading:
- **Issue**: Model unavailable
- **Solution**: Try multiple model variants
- **Fallback Order**: Primary → gpt2 → distilgpt2 → DialoGPT

#### Vector Store:
- **Issue**: Database corruption
- **Solution**: Rebuild from source documents
- **Prevention**: Regular backups and validation

#### PDF Processing:
- **Issue**: Corrupted or unsupported files
- **Solution**: Skip problematic files, log errors
- **Recovery**: Continue processing remaining files

## 📊 Performance Considerations

### Memory Usage:
- **Embeddings**: ~100MB for model loading
- **Vector Store**: Depends on document corpus size
- **LLM**: Variable based on model size
- **Chunking**: Minimal memory footprint

### Processing Speed:
- **Embedding**: ~1-2 seconds per document
- **Vector Search**: <100ms for similarity search
- **LLM Generation**: 2-5 seconds per response
- **PDF Processing**: Depends on document size

### Optimization Tips:
1. Use smaller embedding models for faster inference
2. Implement batch processing for multiple documents
3. Cache embeddings to avoid recomputation
4. Use appropriate chunk sizes for your use case
5. Monitor memory usage during large document processing

---

These components work together to create a robust, scalable, and reliable medical assistant system with comprehensive error handling and fallback mechanisms.
