# 🚀 Quick Start Guide

Get your GenAI Medical Assistant up and running in minutes!

## ⚡ Quick Setup (5 minutes)

### 1. Prerequisites Check
```bash
# Check Python version (3.8+ required)
python --version

# Check pip
pip --version
```

### 2. Environment Setup
```bash
# Navigate to project
cd genai_medical_assistant

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/MacOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Install all requirements
pip install -e .
```

### 4. Configure Environment
Create `.env` file in project root:
```env
HF_TOKEN="your_huggingface_token_here"
HUGGINGFACEHUB_API_TOKEN="your_huggingface_token_here"
```

**Get HuggingFace Token:**
1. Visit [HuggingFace.co](https://huggingface.co/)
2. Create account/Login
3. Go to Settings → Access Tokens
4. Create new token with **write** permissions

### 5. Add Medical Documents
```bash
# Create data directory
mkdir -p data

# Add your PDF medical documents to data/ folder
# Example: copy medical_textbook.pdf to data/
```

### 6. Initialize Vector Database
```python
# Run this Python script to initialize
python -c "
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store

print('Loading PDF documents...')
documents = load_pdf_files()

if documents:
    print(f'Processing {len(documents)} documents...')
    text_chunks = create_text_chunks(documents)
    print(f'Creating vector store from {len(text_chunks)} chunks...')
    vector_store = save_vector_store(text_chunks)
    print('✅ Vector store initialized successfully!')
else:
    print('❌ No PDF documents found in data/ folder')
    print('Please add PDF files to data/ directory first')
"
```

### 7. Start the Application
```bash
# Run the medical assistant
python app/app.py
```

🎉 **Success!** Open http://localhost:5000 in your browser

---

## 🔧 Detailed Setup

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Required for model downloads

### Installation Options

#### Option 1: Standard Installation
```bash
# Clone/download project
cd genai_medical_assistant

# Create environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Development Installation
```bash
# Same as above, plus:
pip install -e .  # Editable installation

# Install development tools
pip install pytest pytest-cov black flake8
```

#### Option 3: Docker Installation (Coming Soon)
```bash
# Build image
docker build -t medical-assistant .

# Run container
docker run -p 5000:5000 medical-assistant
```

### Configuration Options

#### Basic Configuration (`app/config/config.py`)
```python
# Model settings
HUGGINGFACE_REPO_ID = "gpt2"  # Change LLM model
CHUNK_SIZE = 500              # Text chunk size
CHUNK_OVERLAP = 50            # Chunk overlap

# Paths
DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "data/"
```

#### Advanced Configuration
```python
# Embedding model priority (in embeddings.py)
EMBEDDING_MODELS = [
    "sentence-transformers/all-MiniLM-L6-v2",      # Fast, good quality
    "sentence-transformers/all-mpnet-base-v2",     # High quality, slower
    "sentence-transformers/paraphrase-MiniLM-L6-v2" # Alternative
]

# LLM model priority (in llm.py)
LLM_MODELS = [
    "gpt2",                          # Reliable
    "distilgpt2",                    # Faster
    "microsoft/DialoGPT-small"       # Conversational
]
```

---

## 🧪 Verification & Testing

### Quick Health Check
```bash
# Navigate to debugging folder
cd debugging

# Run comprehensive test
python test_complete_fix.py
```

**Expected Output:**
```
🚀 Starting comprehensive embedding and vector store tests...
🧪 Testing embedding model...
✅ Successfully loaded embedding model
🗃️ Testing vector store creation...
✅ Successfully created vector store
🎉 All tests passed!
```

### Individual Component Tests
```bash
# Test embeddings only
python debugging/test_embedding_fix.py

# Test authentication
python debugging/setup_huggingface_auth.py

# Basic functionality test
python debugging/simple_test.py
```

### Troubleshooting Common Issues

#### Issue: "No PDF documents found"
```bash
# Solution: Add PDFs to data folder
mkdir -p data
# Copy your medical PDFs to data/ directory
```

#### Issue: "Authentication failed"
```bash
# Check your .env file
cat .env

# Verify token format (should start with 'hf_')
# Get new token from https://huggingface.co/settings/tokens
```

#### Issue: "Model loading failed"
```bash
# Test with fallback models
python debugging/diagnose_embedding.py

# Check internet connection
ping huggingface.co
```

#### Issue: "Vector store creation failed"
```bash
# Check disk space
df -h  # Linux/macOS
dir   # Windows

# Check permissions
ls -la vectorstore/  # Linux/macOS
```

---

## 🎯 Usage Examples

### Basic Medical Queries
Once running at http://localhost:5000, try these queries:

1. **General Medical Questions:**
   - "What are the symptoms of diabetes?"
   - "How is hypertension treated?"
   - "What causes pneumonia?"

2. **Specific Medical Information:**
   - "Explain the side effects of aspirin"
   - "What is the normal blood pressure range?"
   - "How is COVID-19 diagnosed?"

3. **Treatment and Medication:**
   - "What are treatment options for depression?"
   - "How does insulin work in diabetes?"
   - "What antibiotics treat pneumonia?"

### API Usage (Future)
```bash
# Direct API calls (when implemented)
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is diabetes?"}'
```

---

## 🔄 Maintenance

### Regular Updates
```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Update models (if needed)
# Models are cached locally after first download
```

### Vector Store Maintenance
```bash
# Rebuild vector store (if documents change)
python -c "
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store
import shutil

# Remove old vector store
shutil.rmtree('vectorstore/db_faiss', ignore_errors=True)

# Rebuild
documents = load_pdf_files()
chunks = create_text_chunks(documents)
save_vector_store(chunks)
print('Vector store rebuilt!')
"
```

### Log Monitoring
```bash
# View application logs
tail -f logs/log_$(date +%Y-%m-%d).log

# Check for errors
grep -i error logs/*.log
```

---

## 🆘 Getting Help

### Self-Help Resources
1. **Check Logs**: `logs/log_YYYY-MM-DD.log`
2. **Run Diagnostics**: `python debugging/diagnose_embedding.py`
3. **Test Components**: `python debugging/test_complete_fix.py`

### Common Solutions
- **Restart**: Close and restart the application
- **Clear Cache**: Delete and recreate virtual environment
- **Rebuild Vector Store**: Delete `vectorstore/` and reinitialize
- **Update Token**: Get fresh HuggingFace token

### Debug Mode
```bash
# Run with debug information
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development     # Windows
python app/app.py
```

---

## 🎉 Success Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] `.env` file configured with valid HF token
- [ ] PDF documents added to `data/` folder
- [ ] Vector store initialized successfully
- [ ] Application starts without errors
- [ ] Web interface accessible at http://localhost:5000
- [ ] Test queries return relevant responses
- [ ] All diagnostic tests pass

**Congratulations! Your GenAI Medical Assistant is ready to use! 🎊**

---

*For advanced configuration and development setup, see the main README.md file.*
