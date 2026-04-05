from transformers import pipeline
from datasets import load_dataset
import pandas as pd

print("Loading model...")
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)
languages = {
    "ta": "tam_Taml",
    "hi": "hin_Deva",
    "te": "tel_Telu",
    "kn": "kan_Knda",
    "ml": "mal_Mlym"
}

results = []

print("Processing datasets...\n")

for lang_code, model_code in languages.items():

    print(f"\nLoading dataset for {lang_code}...")

    dataset = load_dataset(
        "ai4bharat/samanantar",
        lang_code,
        split="train[:5]"
    )

    for sample in dataset:
        english = sample["src"][:200]

        output = translator(
            english,
            src_lang="eng_Latn",
            tgt_lang=model_code
        )

        results.append({
            "language": lang_code,
            "english_text": english,
            "translated_text": output[0]["translation_text"]
        })
df = pd.DataFrame(results)
df.to_csv("indic_translation_all_languages.csv", index=False)

print("\nSaved to indic_translation_all_languages.csv")