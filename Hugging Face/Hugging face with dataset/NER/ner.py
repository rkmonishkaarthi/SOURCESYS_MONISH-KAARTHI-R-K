import pandas as pd
from transformers import pipeline

print("Loading dataset...")
df = pd.read_csv("ner_dataset.csv", encoding="latin1")

df["Sentence #"] = df["Sentence #"].ffill()

df = df.dropna(subset=["Word"])

df["Word"] = df["Word"].astype(str)

sentences = df.groupby("Sentence #")["Word"].apply(list)

sentences = [" ".join(words) for words in sentences]

print("Total sentences:", len(sentences))

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

results = []

for text in sentences[:30]:
    output = ner(text)

    for entity in output:
        results.append({
            "sentence": text,
            "entity": entity["word"],
            "label": entity["entity_group"],
            "score": entity["score"]
        })

pd.DataFrame(results).to_csv("ner_results.csv", index=False)

print("Saved to ner_results.csv")