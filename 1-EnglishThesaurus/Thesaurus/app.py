import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data: # cause most of words in data.json are lowercase
        return data[w]
    elif w.title() in data: # for words with first capital letter like Texas
        return data[w.title()]
    elif w.upper() in data: # for words all uppercase like USA, NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(w, data.keys())[0]) 
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry." 
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word:")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)