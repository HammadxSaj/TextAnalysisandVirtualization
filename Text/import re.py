import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# The process text function removes all non-alphabetic characters and converts the text to lowercase.
def process_text(text):
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return clean_text

# The word frequency function splits the text into words, removes stopwords, and counts the frequency of each word forming a dictionary.


def word_frequency(text):
    words = process_text(text).split()
    stopwords = set(["the", "and", "is", "of", "in",
                    "to", "it", "that", "as", "a"])
    filtered_words = [word for word in words if word not in stopwords]
    word_counts = Counter(filtered_words)
    return word_counts

# The generate word cloud function generates a word cloud from the word frequency dictionary.


def generate_word_cloud(text):
    word_freq = word_frequency(text)
    wordcloud = WordCloud(
        width=800, height=800, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# The top n words function returns the top n words from the word frequency dictionary.


def top_n_words(text, n):
    word_freq = word_frequency(text)
    top_words = word_freq.most_common(n)
    return top_words


# Read the text from a file into a string

with open('text_document.txt', 'r', encoding='utf-8') as file:
    document_text = file.read()

# Perform the tasks
print("Top 10 words:")
print(top_n_words(document_text, 10))
generate_word_cloud(document_text)
