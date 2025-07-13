# 👩‍💻 Development Guide

Comprehensive guide for developers working on the GenAI Medical Assistant project, including setup, architecture, best practices, and contribution guidelines.

## 🏗️ Development Environment Setup

### Prerequisites
- Python 3.8+
- Git
- Code editor (VS Code recommended)
- Virtual environment tools

### Initial Setup
```bash
# Clone the repository
git clone <repository-url>
cd genai_medical_assistant

# Create development environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Development Dependencies
```bash
# Core development tools
pip install pytest pytest-cov black flake8 mypy
pip install pre-commit isort bandit safety

# Documentation tools
pip install sphinx sphinx-rtd-theme

# Testing tools
pip install factory-boy faker responses

# Optional: Jupyter for experimentation
pip install jupyter notebook
```

---

## 🏛️ Architecture Overview

### High-Level Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │   Application   │    │   ML Pipeline  │
│                 │    │                 │    │                 │
│  • Flask App    │◄──►│  • RAG Chain    │◄──►│  • Embeddings   │
│  • Templates    │    │  • Retriever    │    │  • Vector Store │
│  • Static Files │    │  • Config       │    │  • LLM          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Architecture
```
app/
├── app.py              # Flask application & routing
├── components/         # Core ML components
│   ├── embeddings.py   # Embedding model management
│   ├── llm.py         # Language model handling
│   ├── pdf_loader.py  # Document processing
│   ├── retriever.py   # RAG implementation
│   └── vector_store.py # Vector database operations
├── config/            # Configuration management
├── common/            # Shared utilities
└── templates/         # Web interface templates
```

### Data Flow
```
PDF Documents → Text Chunks → Embeddings → Vector Store
                                               ↓
User Query → Query Embedding → Similarity Search → Context
                                               ↓
Context + Query → LLM → Response → User Interface
```

---

## 🔧 Development Workflow

### Code Style & Standards

#### Python Code Style
```python
# Use Black for formatting
black app/ debugging/

# Use isort for imports
isort app/ debugging/

# Use flake8 for linting
flake8 app/ debugging/

# Use mypy for type checking
mypy app/
```

#### Code Structure Example
```python
"""
Module docstring explaining purpose and usage.
"""

from typing import List, Optional, Dict, Any
import logging

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)


class ComponentClass:
    """Class docstring with usage examples."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize component with configuration."""
        self.config = config
        self._initialized = False
    
    def process_data(self, data: List[str]) -> Optional[List[str]]:
        """
        Process input data and return results.
        
        Args:
            data: List of strings to process
            
        Returns:
            Processed data or None if processing fails
            
        Raises:
            CustomException: When processing fails
        """
        try:
            logger.info(f"Processing {len(data)} items")
            # Processing logic here
            return processed_data
        except Exception as e:
            error_msg = CustomException("Processing failed", e)
            logger.error(str(error_msg))
            raise error_msg
```

### Git Workflow

#### Branch Strategy
```bash
# Main branches
main        # Production-ready code
develop     # Integration branch for features

# Feature branches
feature/embedding-improvements
feature/new-model-support
feature/web-ui-enhancement

# Bug fix branches
bugfix/authentication-issue
bugfix/memory-leak-fix

# Release branches
release/v1.1.0
```

#### Commit Convention
```bash
# Format: type(scope): description

# Types:
feat(embeddings): add support for custom embedding models
fix(auth): resolve HuggingFace token validation issue
docs(readme): update installation instructions
test(vector): add comprehensive vector store tests
refactor(llm): improve model loading with better error handling
perf(search): optimize vector similarity search performance
```

### Development Process

#### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes with proper testing
# Write/update tests
# Update documentation

# Commit changes
git add .
git commit -m "feat(component): add new feature"

# Push and create pull request
git push origin feature/new-feature
```

#### 2. Testing Strategy
```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Run system tests
python debugging/test_complete_fix.py

# Run with coverage
pytest --cov=app tests/

# Run specific test categories
pytest -m "unit"
pytest -m "integration"
pytest -m "slow"
```

#### 3. Code Review Process
- All changes require pull request review
- Automated checks must pass (tests, linting, security)
- Manual review for architecture and logic
- Documentation updates required for user-facing changes

---

## 🧪 Testing Framework

### Test Structure
```
tests/
├── unit/                  # Unit tests for individual components
│   ├── test_embeddings.py
│   ├── test_llm.py
│   ├── test_vector_store.py
│   └── test_pdf_loader.py
├── integration/           # Integration tests
│   ├── test_rag_chain.py
│   └── test_web_api.py
├── fixtures/             # Test data and fixtures
│   ├── sample_documents/
│   └── mock_responses.py
└── conftest.py           # Pytest configuration
```

### Test Examples

#### Unit Test Example
```python
import pytest
from unittest.mock import Mock, patch
from app.components.embeddings import get_embedding_model

class TestEmbeddingModel:
    """Test embedding model functionality."""
    
    @patch('app.components.embeddings.HuggingFaceEmbeddings')
    def test_get_embedding_model_success(self, mock_embeddings):
        """Test successful embedding model loading."""
        mock_model = Mock()
        mock_embeddings.return_value = mock_model
        
        result = get_embedding_model()
        
        assert result == mock_model
        mock_embeddings.assert_called_once()
    
    def test_embedding_generation(self):
        """Test embedding generation functionality."""
        model = get_embedding_model()
        test_text = "Sample medical text"
        
        embedding = model.embed_query(test_text)
        
        assert isinstance(embedding, list)
        assert len(embedding) > 0
        assert all(isinstance(x, float) for x in embedding)

@pytest.mark.integration
class TestRAGChain:
    """Integration tests for RAG chain."""
    
    def test_end_to_end_query(self):
        """Test complete query processing workflow."""
        from app.components.retriever import create_qa_chain
        
        qa_chain = create_qa_chain()
        result = qa_chain.invoke({"input": "What is diabetes?"})
        
        assert "answer" in result
        assert len(result["answer"]) > 0
```

#### Fixture Examples
```python
# conftest.py
import pytest
from pathlib import Path

@pytest.fixture
def sample_documents():
    """Provide sample documents for testing."""
    return [
        "Sample medical document about diabetes.",
        "Information about hypertension treatment.",
        "Symptoms and diagnosis of pneumonia."
    ]

@pytest.fixture
def test_config():
    """Provide test configuration."""
    return {
        "HF_TOKEN": "test_token",
        "CHUNK_SIZE": 100,
        "CHUNK_OVERLAP": 20,
        "DB_FAISS_PATH": "test_vectorstore/"
    }

@pytest.fixture(autouse=True)
def cleanup_test_files():
    """Clean up test files after each test."""
    yield
    # Cleanup code here
    test_paths = ["test_vectorstore/", "test_logs/"]
    for path in test_paths:
        if Path(path).exists():
            shutil.rmtree(path)
```

---

## 📊 Performance & Monitoring

### Performance Testing
```python
import time
import psutil
import pytest

@pytest.mark.performance
def test_embedding_performance():
    """Test embedding generation performance."""
    from app.components.embeddings import get_embedding_model
    
    model = get_embedding_model()
    test_texts = ["Sample text"] * 100
    
    start_time = time.time()
    embeddings = model.embed_documents(test_texts)
    duration = time.time() - start_time
    
    # Performance assertions
    assert duration < 30.0  # Should complete in 30 seconds
    assert len(embeddings) == 100
    
    # Memory usage check
    process = psutil.Process()
    memory_mb = process.memory_info().rss / 1024 / 1024
    assert memory_mb < 2048  # Should use less than 2GB

@pytest.mark.performance
def test_vector_search_performance():
    """Test vector search performance."""
    # Similar performance testing for vector operations
    pass
```

### Monitoring Integration
```python
# In app/common/monitoring.py
import time
import functools
from typing import Callable

def monitor_performance(func: Callable) -> Callable:
    """Decorator to monitor function performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        
        logger.info(f"{func.__name__} completed in {duration:.2f}s")
        
        # Send metrics to monitoring system
        # metrics.timing(f"{func.__name__}.duration", duration)
        
        return result
    return wrapper
```

---

## 🛡️ Security & Best Practices

### Security Guidelines

#### Environment Variables
```python
# ✅ Good: Use environment variables for secrets
HF_TOKEN = os.environ.get("HF_TOKEN")

# ❌ Bad: Hard-code secrets
HF_TOKEN = "hf_hardcoded_token_here"

# ✅ Good: Validate environment variables
def validate_config():
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN environment variable is required")
    if not HF_TOKEN.startswith("hf_"):
        raise ValueError("Invalid HF_TOKEN format")
```

#### Input Validation
```python
def validate_user_input(query: str) -> str:
    """Validate and sanitize user input."""
    if not query or not query.strip():
        raise ValueError("Query cannot be empty")
    
    # Length limits
    if len(query) > 1000:
        raise ValueError("Query too long (max 1000 characters)")
    
    # Content filtering
    forbidden_patterns = ["<script>", "javascript:", "data:"]
    for pattern in forbidden_patterns:
        if pattern.lower() in query.lower():
            raise ValueError("Query contains forbidden content")
    
    return query.strip()
```

#### Error Handling
```python
# ✅ Good: Proper error handling
try:
    result = dangerous_operation()
except SpecificException as e:
    logger.error(f"Specific error occurred: {e}")
    raise CustomException("User-friendly message") from e
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise CustomException("Something went wrong") from e

# ❌ Bad: Catching all exceptions without proper handling
try:
    result = dangerous_operation()
except:
    pass  # Silent failure
```

### Code Quality Tools

#### Pre-commit Configuration
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
  
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
  
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.4
    hooks:
      - id: bandit
        args: ['-r', '.']
  
  - repo: https://github.com/Lucas-C/pre-commit-hooks-safety
    rev: v1.3.0
    hooks:
      - id: python-safety-dependencies-check
```

---

## 📚 Documentation

### Code Documentation
```python
def complex_function(
    input_data: List[Dict[str, Any]],
    config: Optional[Dict[str, str]] = None,
    timeout: float = 30.0
) -> Tuple[bool, List[str]]:
    """
    Process complex input data with configuration.
    
    This function performs complex processing on input data using the provided
    configuration. It includes timeout handling and comprehensive error reporting.
    
    Args:
        input_data: List of dictionaries containing the data to process.
                   Each dictionary must have 'id' and 'content' keys.
        config: Optional configuration dictionary. If None, uses defaults.
               Supported keys: 'model_name', 'batch_size', 'temperature'.
        timeout: Maximum time in seconds to wait for processing completion.
    
    Returns:
        Tuple of (success: bool, results: List[str])
        - success: True if processing completed successfully
        - results: List of processed results or error messages
    
    Raises:
        ValueError: If input_data is empty or contains invalid items
        TimeoutError: If processing exceeds the specified timeout
        CustomException: For other processing errors
    
    Example:
        >>> data = [{'id': '1', 'content': 'Sample text'}]
        >>> config = {'model_name': 'gpt2', 'batch_size': 32}
        >>> success, results = complex_function(data, config)
        >>> print(f"Success: {success}, Results: {len(results)}")
        Success: True, Results: 1
    """
    # Implementation here
    pass
```

### API Documentation
```python
# Use docstring format for Flask routes
@app.route('/api/query', methods=['POST'])
def api_query():
    """
    Process medical query and return AI response.
    
    Request Body:
        {
            "query": "Medical question string",
            "context_k": 3,  // Optional: number of context documents
            "temperature": 0.3  // Optional: response creativity
        }
    
    Response:
        {
            "success": true,
            "answer": "AI response string",
            "context": ["relevant document excerpts"],
            "timestamp": "2023-07-13T10:30:00Z"
        }
    
    Error Response:
        {
            "success": false,
            "error": "Error description",
            "error_code": "INVALID_QUERY"
        }
    
    Status Codes:
        200: Success
        400: Invalid request
        500: Internal server error
    """
    pass
```

---

## 🚀 Deployment & CI/CD

### GitHub Actions Workflow
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    
    - name: Run linting
      run: |
        flake8 app/ debugging/
        black --check app/ debugging/
        isort --check-only app/ debugging/
    
    - name: Run security checks
      run: |
        bandit -r app/
        safety check
    
    - name: Run tests
      run: |
        pytest tests/ --cov=app --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

### Docker Configuration
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY debugging/ ./debugging/

# Create necessary directories
RUN mkdir -p data/ logs/ vectorstore/

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run application
CMD ["python", "app/app.py"]
```

---

## 🤝 Contributing Guidelines

### Pull Request Process

1. **Fork and Branch**
   ```bash
   git fork <repository>
   git checkout -b feature/your-feature
   ```

2. **Development**
   - Write code following style guidelines
   - Add/update tests for new functionality
   - Update documentation as needed
   - Ensure all tests pass locally

3. **Pre-submission Checklist**
   - [ ] Code follows style guidelines (Black, isort, flake8)
   - [ ] All tests pass (`pytest`)
   - [ ] Security checks pass (`bandit`, `safety`)
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated (if applicable)

4. **Submit Pull Request**
   - Clear title and description
   - Reference related issues
   - Include testing instructions
   - Request appropriate reviewers

### Issue Templates

#### Bug Report Template
```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected Behavior**
What you expected to happen.

**Environment**
- OS: [e.g. Windows 10]
- Python Version: [e.g. 3.9]
- Package Version: [e.g. 1.0.0]

**Additional Context**
Add any other context about the problem here.
```

#### Feature Request Template
```markdown
**Feature Description**
A clear description of what you want to happen.

**Problem Statement**
Describe the problem this feature would solve.

**Proposed Solution**
Describe the solution you'd like to see.

**Alternative Solutions**
Describe alternatives you've considered.

**Additional Context**
Add any other context or screenshots about the feature request here.
```

---

## 📈 Performance Optimization

### Profiling Tools
```python
# Performance profiling
import cProfile
import pstats

def profile_function(func):
    """Profile a function's performance."""
    pr = cProfile.Profile()
    pr.enable()
    
    result = func()
    
    pr.disable()
    stats = pstats.Stats(pr)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
    
    return result
```

### Memory Optimization
```python
# Memory usage monitoring
import tracemalloc
import gc

def monitor_memory(func):
    """Monitor memory usage of a function."""
    tracemalloc.start()
    
    # Measure before
    snapshot1 = tracemalloc.take_snapshot()
    
    result = func()
    
    # Force garbage collection
    gc.collect()
    
    # Measure after
    snapshot2 = tracemalloc.take_snapshot()
    
    # Calculate difference
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    for stat in top_stats[:10]:
        print(stat)
    
    tracemalloc.stop()
    return result
```

---

This development guide provides comprehensive information for contributing to and maintaining the GenAI Medical Assistant project. Follow these guidelines to ensure code quality, maintainability, and project success.
