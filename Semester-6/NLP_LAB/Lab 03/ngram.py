import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from collections import defaultdict
import math

# Download required NLTK data
nltk.download("punkt")
nltk.download("brown")

# Load corpus words
data = brown.words()
tokens = [word.lower() for word in data if word.isalpha()]

# ---------- CREATE N-GRAM ----------
def create_ngram(words, n):
    model = defaultdict(dict)

    for i in range(len(words) - n):
        context = tuple(words[i:i+n-1])
        next_word = words[i+n-1]

        if next_word in model[context]:
            model[context][next_word] += 1
        else:
            model[context][next_word] = 1

    return model

n = 3
ngram = create_ngram(tokens, n)

# ---------- PREDICT NEXT WORD ----------
def predict_next(text):
    words = word_tokenize(text.lower())
    context = tuple(words[-(n-1):])

    if context not in ngram:
        return []

    total = sum(ngram[context].values())
    result = []

    for word, count in ngram[context].items():
        result.append((word, count / total))

    result.sort(key=lambda x: x[1], reverse=True)
    return result[:5]

# ---------- PERPLEXITY ----------
def calculate_perplexity(test_words):
    log_sum = 0
    count = 0

    for i in range(len(test_words) - n):
        context = tuple(test_words[i:i+n-1])
        word = test_words[i+n-1]

        if context in ngram and word in ngram[context]:
            prob = ngram[context][word] / sum(ngram[context].values())
        else:
            prob = 0.000001

        log_sum += math.log(prob)
        count += 1

    return math.exp(-log_sum / count)

# ---------- TEST ----------
sentence = "irregularities took place"
prediction = predict_next(sentence)

print("Next word prediction:")
for w, p in prediction:
    print(w, ":", round(p, 4))

test_sample = tokens[-1000:]
print("Perplexity:", calculate_perplexity(test_sample))

# ---------- AUTO COMPLETE ----------
def sentence_complete(text, limit=15):
    output = text

    for _ in range(limit):
        next_word = predict_next(output)
        if not next_word:
            break
        output += " " + next_word[0][0]

    return output

print("Completed Sentence:")
print(sentence_complete(sentence))