from transformers import pipeline

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

text = "Hello, how are you?"

ta_result = translator(
    text,
    src_lang="eng_Latn",
    tgt_lang="tam_Taml"
)
print("Tamil:", ta_result[0]['translation_text'])

hi_result = translator(
    text,
    src_lang="eng_Latn",
    tgt_lang="hin_Deva"
)
print("Hindi:", hi_result[0]['translation_text'])

ml_result = translator(
    text,
    src_lang="eng_Latn",
    tgt_lang="mal_Mlym"
)
print("Malayalam:", ml_result[0]['translation_text'])

te_result = translator(
    text,
    src_lang="eng_Latn",
    tgt_lang="tel_Telu"
)
print("Telugu:", te_result[0]['translation_text'])

kn_result = translator(
    text,
    src_lang="eng_Latn",
    tgt_lang="kan_Knda"
)
print("Kannada:", kn_result[0]['translation_text'])