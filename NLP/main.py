import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

text = "Artificial Intelligence is transforming industries by enabling machines to learn, reason, and make decisions efficiently."
tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

processed_tokens = [
    lemmatizer.lemmatize(word.lower())
    for word in tokens
    if word.isalnum() and word.lower() not in stop_words
]

word_freq = Counter(processed_tokens)

print("\nNLP Processing Output")
print("Original Text:", text)
print("Tokens:", tokens)
print("Processed Tokens:", processed_tokens)
print("Word Frequency:", word_freq)