import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger_eng")

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

pos = {
    "NN": "Noun",
    "PRP": "Pronoun",
    "VB": "Verb",
    "JJ": "Adjective",
    "RB": "Adverb",
    "IN": "Preposition",
    "CC": "Conjunction",
    "UH": "Interjection"
}

for w, t in tags:
    found = False
    for key in pos:
        if t.startswith(key):
            print(w, ":", pos[key])
            found = True
            break
    if not found:
        print(w, ":", t)
