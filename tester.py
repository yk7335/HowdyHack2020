# api url  = 	https://od-api.oxforddictionaries.com/api/v2
# app id = 	cf5fbd52
# app keys = fce114074fe457c58747c183ca2a4b8f

#https://od-api.oxforddictionaries.com/api/v2/thesaurus/en/bitch?strictMatch=false



# import json
# import requests
# app_id  = "<cf5fbd52>"
# app_key  = "<fce114074fe457c58747c183ca2a4b8f>"
# endpoint = "entries"
# language_code = "en-us"
# word_id = "sad"
# url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
# r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))

# import requests

# url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# querystring = {"term":"yash"}

# headers = {
#     'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
#     'x-rapidapi-key': "b5e4df438emsh32b66ffc959025cp110199jsn301794ffaf6b"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
#Creating a list 
synonyms = []
for syn in wordnet.synsets("bitch"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())#adding into synonyms
print (set(synonyms))