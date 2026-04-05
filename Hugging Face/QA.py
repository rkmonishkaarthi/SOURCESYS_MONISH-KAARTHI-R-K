from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

result = qa(
    question="Who is the CEO of Tesla?",
    context="Elon Musk is the CEO of Tesla and SpaceX."
)

print(result)