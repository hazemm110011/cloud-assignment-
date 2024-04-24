import nltk
import os


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')


file_path = '/app/paragraphs.txt'


if not os.path.exists(file_path):
    print(f"Error: File not found at '{file_path}'")
else:
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()




with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = word_tokenize(text.lower())

english_stopwords = set(stopwords.words('english'))

filtered_words = [word for word in words if word.isalpha() and word not in english_stopwords]

word_counts = Counter(filtered_words)

print("Word Frequency Count:")
for word, count in word_counts.items():
    print(f"{word}: {count}")