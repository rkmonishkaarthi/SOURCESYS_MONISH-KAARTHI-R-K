from transformers import pipeline
from datasets import load_dataset
import pandas as pd

print("Loading dataset...")
dataset = load_dataset("squad")

print("Loading QA model...")
qa = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

results = []

print("Processing data...\n")

for sample in dataset["train"].select(range(30)):
    
    question = sample["question"]
    context = sample["context"]
    
    output = qa(
        question=question,
        context=context
    )
    
    results.append({
        "question": question,
        "context": context[:200],
        "predicted_answer": output["answer"],
        "confidence_score": output["score"]
    })

df = pd.DataFrame(results)

df.to_csv("qa_results.csv", index=False)

print("\nResults saved to qa_results.csv")