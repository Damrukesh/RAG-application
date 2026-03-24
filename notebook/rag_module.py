# RAG Module - Extract functions from notebook for import

import sys
import os
from pathlib import Path

# Add the notebook directory to path
notebook_dir = Path(__file__).parent
sys.path.insert(0, str(notebook_dir))

# Import the functions from the notebook
try:
    from doc import EmbeddingManager, VectorStore, retrieve_relevant_chunks
    from langchain_core.documents import Document
    import numpy as np
    
    # Re-export for easy importing
    __all__ = [
        'EmbeddingManager', 
        'VectorStore', 
        'retrieve_relevant_chunks',
        'Document',
        'np'
    ]
    
    print("✅ RAG module loaded successfully!")
    
except ImportError as e:
    print(f"❌ Error importing from notebook: {e}")
    
    # Create dummy functions if import fails
    class EmbeddingManager:
        def __init__(self, *args, **kwargs):
            raise ImportError("RAG module not available - check notebook")
    
    class VectorStore:
        def __init__(self, *args, **kwargs):
            raise ImportError("RAG module not available - check notebook")
    
    def retrieve_relevant_chunks(*args, **kwargs):
        raise ImportError("RAG module not available - check notebook")
