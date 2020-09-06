import json
from adjectives import* 
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet



def LookThisUp(dictionary,string):
    return dictionary.get(string)
    
    



def ParseEntry(string):
    synonyms = []
    count = 0
    JournalList = string.split(" ")
    for word in JournalList:
        if LookThisUp(adjDict,word) == 'sad_words':
                count += -2
        if LookThisUp(adjDict,word) == 'mad_words':
            count += -1
        if LookThisUp(adjDict,word) == 'anx_words':
            count += 1
        if LookThisUp(adjDict,word) == 'hap_words':
            count += 2
        if LookThisUp(adjDict,word) != 'mad_words' and LookThisUp(adjDict,word) != 'anx_words' and LookThisUp(adjDict,word) != 'sad_words' and LookThisUp(adjDict,word) != 'hap_words':
            for syn in wordnet.synsets(word):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())#adding into synonyms
            for syno in synonyms:
                if LookThisUp(adjDict,syno) == 'sad_words':
                    count += -2
                    break
                if LookThisUp(adjDict,syno) == 'mad_words':
                    count += -1
                    break
                if LookThisUp(adjDict,syno) == 'anx_words':
                    count += 1
                    break
                if LookThisUp(adjDict,syno) == 'hap_words':
                    count += 2
                    break

    return count









