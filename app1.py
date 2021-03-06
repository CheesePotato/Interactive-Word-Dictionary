import json
import difflib
from difflib import get_close_matches


data = json.load(open('C:\\Users\\Wel\\Python Apps\\App1\\data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0 :
        q = input("Did you mean %s instead? Enter Y if yes, or N if no:  " % get_close_matches(word,data.keys())[0])
        if q == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif q == 'N':
            return "Double check your word"
        else :
            return "Your query couldn't be processed"
    else:
        return('Please check the word and enter again')
word = input("Enter Word:  ")

output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
