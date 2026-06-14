"""
Step 3 - Document Ingestion & Chunking
RAG Pipeline for CS Survival Tips

Loads .txt files from documents/, cleans them, and splits into
500-character chunks with 50-character overlap.
"""

import os
import glob

DOCUMENTS_DIR = "documents"
CHUNK_SIZE = 500
OVERLAP = 50


def clean_text(text: str) -> str:
    """Remove extra whitespace and blank lines."""
    lines = text.splitlines()
    cleaned = [line.strip() for line in lines if line.strip()]
    return " ".join(cleaned)


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    """
    Split text into chunks of `chunk_size` characters with `overlap` characters
    of overlap between consecutive chunks.
    """
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():  # skip empty chunks
            chunks.append(chunk)
        # Move forward by (chunk_size - overlap) so next chunk shares `overlap` chars
        start += chunk_size - overlap

    return chunks


def load_documents(directory: str) -> list[dict]:
    """Load all .txt files from `directory` and return list of {source, text} dicts."""
    pattern = os.path.join(directory, "*.txt")
    file_paths = sorted(glob.glob(pattern))

    if not file_paths:
        raise FileNotFoundError(f"No .txt files found in '{directory}/'")

    documents = []
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        cleaned = clean_text(raw)
        documents.append({"source": os.path.basename(path), "text": cleaned})
        print(f"  Loaded: {os.path.basename(path)} ({len(cleaned)} chars after cleaning)")

    return documents


def main():
    print(f"=== RAG Step 3: Ingestion & Chunking ===\n")
    print(f"Settings: chunk_size={CHUNK_SIZE}, overlap={OVERLAP}\n")

    # 1. Load documents
    print(f"Loading documents from '{DOCUMENTS_DIR}/'...")
    documents = load_documents(DOCUMENTS_DIR)
    print(f"\nLoaded {len(documents)} document(s).\n")

    # 2. Chunk all documents
    all_chunks = []
    for doc in documents:
        doc_chunks = chunk_text(doc["text"])
        for i, chunk in enumerate(doc_chunks):
            all_chunks.append({
                "source": doc["source"],
                "chunk_index": i,
                "text": chunk
            })

    # 3. Print 5 sample chunks
    print("--- 5 Sample Chunks ---\n")
    for sample in all_chunks[:5]:
        print(f"[Source: {sample['source']} | Chunk #{sample['chunk_index']}]")
        print(sample["text"])
        print(f"(length: {len(sample['text'])} chars)\n")

    # 4. Total count
    print(f"Total chunks produced: {len(all_chunks)}")

    return all_chunks


if __name__ == "__main__":
    main()
