import chromadb
from sentence_transformers import SentenceTransformer
from ingest import process_documents

# Load embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load and chunk documents
print("Processing documents...")
chunks = process_documents("documents")

# Set up ChromaDB
client = chromadb.Client()
collection = client.create_collection("cs_survival_guide")

# Embed and store chunks
print("Embedding and storing chunks...")
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk["text"]).tolist()
    collection.add(
        ids=[f"chunk_{i}"],
        embeddings=[embedding],
        documents=[chunk["text"]],
        metadatas=[{"source": chunk["source"], "chunk_index": chunk["chunk_index"]}]
    )

print(f"Stored {len(chunks)} chunks in ChromaDB")

# Test retrieval with 3 queries
test_queries = [
    "How do I prepare before starting a CS degree?",
    "What should CS students learn outside of class?",
    "How hard is it to finish a CS degree?"
]

print("\n--- RETRIEVAL TESTS ---")
for query in test_queries:
    print(f"\nQuery: {query}")
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    for j, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][j]["source"]
        print(f"  Result {j+1} (from {source}):")
        print(f"  {doc[:200]}")
        print()
