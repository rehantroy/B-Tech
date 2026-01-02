from nltk.tokenize import word_tokenize
import nltk
nltk.download("punkt")

pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
determiners = ["the", "a", "an", "this", "that", "these", "those"]
conjunctions = ["and", "or", "but", "so", "yet", "for", "nor"]
prepositions = ["in", "on", "at", "for", "with", "by", "to", "from", "about", "as", "into"]
interjections = ["oh", "wow", "oops", "hey", "alas", "hurray", "ouch"]
verbs_be = ["is", "am", "are", "was", "were", "be", "being", "been"]
irregular_verbs = ["go", "went", "gone", "do", "did", "done", "have", "had", "has"]

text = input("Enter a sentence: ")
words = word_tokenize(text)

for i, w in enumerate(words):
    lw = w.lower()
    pos = "Noun"  
    if lw in [".", ",", "!", "?", ":", ";", "'", '"', "(", ")"]:
        pos = "Punct"
    elif w in pronouns:
        pos = "Pronoun"
    elif lw in determiners:
        pos = "Determiner"
    elif lw in conjunctions:
        pos = "Conjunction"
    elif lw in prepositions:
        pos = "Preposition"
    elif lw in interjections:
        pos = "Interjection"
    elif w in verbs_be or lw.endswith(("ing", "ed")) or lw in irregular_verbs:
        pos = "Verb"
    elif lw.endswith("ly"):
        pos = "Adverb"
    elif lw.endswith(("ous", "ful", "able", "ive", "ic")):
        pos = "Adjective"
    elif i != 0 and w[0].isupper():
        pos = "Proper Noun"
    elif i > 0 and words[i-1].lower() in determiners:
        pos = "Adjective"  #word after determiner is often adjective

    print(w, ":", pos)
