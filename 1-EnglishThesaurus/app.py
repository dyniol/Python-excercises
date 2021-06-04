import json

data = json.load(open("/home/dakar/coding/py/Python-excercises/1-EnglishThesaurus/data.json"))

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))