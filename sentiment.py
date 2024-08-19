import ssl
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Bypass SSL verification
# ssl._create_default_https_context = ssl._create_unverified_context

# Download VADER lexicon
# nltk.download('vader_lexicon')

def analyze_sentiment_vader(filename):
    with open(filename, 'r') as file:
        text = file.read()
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(text)
        return sentiment

# Analyze sentiment for both files
sentiment_new = analyze_sentiment_vader('text_ntest.txt')
sentiment_old = analyze_sentiment_vader('text_otest.txt')


sentiment_09_v1 = analyze_sentiment_vader('speeches/07-09.txt')
sentiment_09_v2 = analyze_sentiment_vader('speeches/07-09_v2.txt')

print(f"Sentiment of new text: {sentiment_09_v1}")
print(f"Sentiment of old fl rally text: {sentiment_09_v2}")






