import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = "Hello everyone. Welcome to day one of LNP Lab."

text = text.lower()
print("After Case Folding:")
print(text)
punct = text.translate(str.maketrans('', '', string.punctuation))
print("\nAfter Punctuation Removal:")
print(punct)

sentences = sent_tokenize(punct)
print("\nSentence Tokenization:")
print(sentences)

tokens = word_tokenize(punct)
print("\nWord Tokenization:")
print(tokens)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print("\nAfter Stopword Removal:")
print(filtered_tokens)
#Stemming can produce non-meaningful words (e.g., "studying" becomes "studi").Lemmatization gives the proper dictionary word (e.g., "studying" becomes "study").


stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print("\nAfter Stemming:")
print(stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\nAfter Lemmatization:")
print(lemmatized_words)
