import os

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "source": filename,
                "text": text
            })
    print(f"Loaded {len(documents)} documents")
    return documents

def clean_text(text):
    import re
    # Remove lines that are just dashes
    text = re.sub(r"^-+$", "", text, flags=re.MULTILINE)
    # Remove brackets
    text = text.replace("[", "").replace("]", "")
    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if len(chunk.strip()) > 50:  # skip tiny chunks
            chunks.append(chunk)
        start = end - overlap
    return chunks

def process_documents(folder_path):
    documents = load_documents(folder_path)
    all_chunks = []
    for doc in documents:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": doc["source"],
                "chunk_index": i,
                "text": chunk
            })
    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks

if __name__ == "__main__":
    chunks = process_documents("documents")
    # Print 5 sample chunks
    print("\n--- SAMPLE CHUNKS ---")
    for chunk in chunks[:5]:
        print(f"\nSource: {chunk['source']}")
        print(f"Chunk {chunk['chunk_index']}:")
        print(chunk['text'])
        print("-" * 40)
