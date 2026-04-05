import pandas as pd
from transformers import pipeline

print("Loading dataset...")
df = pd.read_csv("test.csv")

df.columns = ["label", "title", "description"]

df["text"] = df["title"] + " " + df["description"]

df = df.dropna(subset=["text"])
df["text"] = df["text"].astype(str)

print("Total records:", len(df))

print("Loading model...")
generator = pipeline(
    "text-generation",
    model="gpt2"
)

results = []

print("Processing...\n")

for text in df["text"][:30]:   
    
    prompt = text[:50]   
    
    output = generator(
        prompt,
        max_length=40,
        num_return_sequences=1
    )
    
    results.append({
        "prompt": prompt,
        "generated_text": output[0]["generated_text"]
    })

result_df = pd.DataFrame(results)
result_df.to_csv("text_generation_results.csv", index=False)

print("\nResults saved to text_generation_results.csv")