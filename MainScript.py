import json
from adjectives import* 



def LookThisUp(dictionary,string):
    return dictionary.get(string)
    

def takeJournalEntry():
    Entry = input("Tell us about your day: ")
    return Entry
    



def ParseEntry(string):
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
    return count





EntryScore = 0
Entry = takeJournalEntry()
EntryScore = ParseEntry(Entry)
print(EntryScore)




