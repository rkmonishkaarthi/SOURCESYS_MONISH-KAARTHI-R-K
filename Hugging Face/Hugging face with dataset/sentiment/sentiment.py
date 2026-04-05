import pandas as pd
from transformers import pipeline

print("Loading dataset...")
df = pd.read_csv("IMDB_Dataset.csv")

df = df.dropna(subset=["review"])
df["review"] = df["review"].astype(str)

print("Total records:", len(df))

print("Loading sentiment model...")
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

results = []

print("Processing...\n")

for text in df["review"][:100]:
    
    text = text[:512]
    
    output = sentiment(text)[0]
    
    results.append({
        "review": text[:200],   
        "predicted_sentiment": output["label"],
        "confidence_score": output["score"]
    })

result_df = pd.DataFrame(results)
result_df.to_csv("sentiment_results.csv", index=False)

print("\nResults saved to sentiment_results.csv")