import chromadb
import gradio as gr
from sentence_transformers import SentenceTransformer
from groq import Groq
from ingest import process_documents
import os
from dotenv import load_dotenv

load_dotenv()

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.create_collection("cs_survival_guide")

print("Processing documents...")
chunks = process_documents("documents")
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk["text"]).tolist()
    collection.add(
        ids=[f"chunk_{i}"],
        embeddings=[embedding],
        documents=[chunk["text"]],
        metadatas=[{"source": chunk["source"]}]
    )
print("Ready!")

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    query_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )
    chunks_text = results["documents"][0]
    sources = list(set([m["source"] for m in results["metadatas"][0]]))
    context = "\n\n".join(chunks_text)
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for CS students. Answer questions using ONLY the provided context from Reddit threads. If the context does not contain enough information, say I dont have enough information on that. Always cite which document your answer comes from."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    answer = response.choices[0].message.content
    sources_text = "\n".join(f"- {s}" for s in sources)
    return answer, sources_text

with gr.Blocks() as demo:
    gr.Markdown("# CS Survival Guide")
    gr.Markdown("Ask questions about surviving a CS degree based on real Reddit advice!")
    inp = gr.Textbox(label="Your question", placeholder="e.g. How do I prepare for a CS degree?")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Sources", lines=4)
    btn.click(ask, inputs=inp, outputs=[answer, sources])
    inp.submit(ask, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()
