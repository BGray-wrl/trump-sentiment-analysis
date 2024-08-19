import nltk

# Download stopwords from nltk
nltk.download('stopwords')


from nltk.corpus import stopwords

# Load the English stopwords list
stop_words = stopwords.words('english')
print(stop_words)