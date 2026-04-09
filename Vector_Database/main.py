import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("\n--- Manual Text Search ---")

manual_texts = [
    "Artificial intelligence is changing industries",
    "Data science involves statistics and programming",
    "Neural networks are used in deep learning",
    "Big data helps in making better decisions"
]

manual_vectors = model.encode(manual_texts).astype("float32")

index1 = faiss.IndexFlatL2(manual_vectors.shape[1])
index1.add(manual_vectors)

query = "what is neural network"
query_vec = model.encode([query]).astype("float32")

dist, idx = index1.search(query_vec, 2)

for i in idx[0]:
    print(manual_texts[i])

print("\n--- File Text Search ---")

with open("text.txt", "r", encoding="utf-8") as f:
    file_texts = [line.strip() for line in f if line.strip()]

file_vectors = model.encode(file_texts).astype("float32")

index2 = faiss.IndexFlatL2(file_vectors.shape[1])
index2.add(file_vectors)

query2 = "applications of ai"
query_vec2 = model.encode([query2]).astype("float32")

dist2, idx2 = index2.search(query_vec2, 2)

for i in idx2[0]:
    print(file_texts[i])

print("\n--- Combined Search ---")

all_texts = manual_texts + file_texts

all_vectors = model.encode(all_texts).astype("float32")

index3 = faiss.IndexFlatL2(all_vectors.shape[1])
index3.add(all_vectors)

query3 = "data science techniques"
query_vec3 = model.encode([query3]).astype("float32")

dist3, idx3 = index3.search(query_vec3, 3)

for i in idx3[0]:
    print(all_texts[i])