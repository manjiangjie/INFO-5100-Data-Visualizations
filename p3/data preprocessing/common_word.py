import pandas,re
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wb = pandas.read_json('../data/wordBank.json')['word'].unique()

def comparison(wordbank, text):
    print("common word")
    common = set(wordbank)&text
    print(common)
    print("word in text but not in wordbank")
    not_common = res - set(wordbank)
    print(not_common)
    print("Coverage rate:"  + str(len(common)/len(text)))

unlemmatized = set(re.sub(",|\.+|“|”|!|/r|/n|\"|\?"," ",open("../data/story.txt").read().lower()).split(" "))

res = set([])
for u in unlemmatized:
    converted = wordnet_lemmatizer.lemmatize(u)
    res.add(converted)

comparison(wb, unlemmatized)

