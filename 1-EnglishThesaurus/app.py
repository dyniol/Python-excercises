import json

data = json.load(open("1-EnglishThesaurus\data.json"))

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))