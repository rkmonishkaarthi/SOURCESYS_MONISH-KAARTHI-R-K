import pandas as pd
from transformers import pipeline

print("Loading dataset...")
df = pd.read_csv("test.csv")

df = df.dropna(subset=["article"])
df["article"] = df["article"].astype(str)

print("Total records:", len(df))

print("Loading summarization model...")
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

results = []

print("Processing...\n")

for text in df["article"][:5]:
    
    text = text[:1000]
    
    output = summarizer(
        text,
        max_length=50,
        min_length=20,
        do_sample=False
    )
    
    results.append({
        "article": text[:200],
        "generated_summary": output[0]["summary_text"]
    })


result_df = pd.DataFrame(results)
result_df.to_csv("summarization_results.csv", index=False)

print("\nResults saved to summarization_results.csv")