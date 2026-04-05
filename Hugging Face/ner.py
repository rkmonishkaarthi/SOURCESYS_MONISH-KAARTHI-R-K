from transformers import pipeline

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

text = "Sundar Pichai is the CEO of Google and lives in California"

result = ner(text)

for entity in result:
    print(entity)