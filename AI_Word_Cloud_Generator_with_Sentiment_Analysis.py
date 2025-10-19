# Quick start
# 1. Takes a paragraph or text file as input.
# 2. Analyzes the sentiment (positive, negative, neutral).
# 3. Generates a word cloud visualization based on word frequency.

# AI Word Cloud Generator with Sentiment Analysis
# -----------------------------------------------
# Libraries: nltk (for sentiment), wordcloud, matplotlib

from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive 😊", sentiment_score
    elif sentiment_score < 0:
        return "Negative 😞", sentiment_score
    else:
        return "Neutral 😐", sentiment_score

def generate_wordcloud(text):
    stopwords = set(STOPWORDS)
    wc = WordCloud(width=800, height=400, background_color='white',
                   stopwords=stopwords, colormap='viridis').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud", fontsize=16)
    plt.show()

def main():
    print("🧠 AI Word Cloud & Sentiment Analyzer 🧠")
    print("----------------------------------------")
    choice = input("Enter 1 to type text or 2 to load from a file: ")

    if choice == '1':
        text = input("\nEnter your paragraph:\n")
    elif choice == '2':
        file_path = input("Enter file path: ")
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        print("Invalid choice.")
        return

    sentiment, score = analyze_sentiment(text)
    print(f"\nDetected Sentiment: {sentiment} (Score: {score:.2f})")

    print("\nGenerating Word Cloud...")
    generate_wordcloud(text)

if __name__ == "__main__":
    main()
