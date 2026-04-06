from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "I love cricket",
    "I enjoy playing sports",
    "The sky is blue",
    "Artificial intelligence is transforming the world",
    "Machine learning helps computers learn from data",
    "I like reading books in my free time",
    "The weather is very pleasant today",
    "He is working on a new project",
    "Technology is evolving rapidly",
    "She enjoys listening to music",
    "Data science is an interesting field",
    "Python is a popular programming language",
    "Traveling helps you explore new cultures"
]

embeddings = model.encode(sentences)

print(embeddings)