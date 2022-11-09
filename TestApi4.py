from pprint import pprint

import requests

app_id = "7cb38fcc"
app_key = 'f2d92f92a152cc7a33e4531636544add'

language = 'en-gb'
word_id = 'have'
fields = 'pronunciations'
strictMatch = 'false'

url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
res=r.json()['results']

listLexicalEntries =[]

for i in res:
    listLexicalEntries.append(i['lexicalEntries'])

listEntries = []
for i in listLexicalEntries:
    for j in i:
       listEntries.append(j['entries'])
# listPronunciations = []
# for i in listEntries:
#     for j in i:
#        listPronunciations.append(j['pronunciations'][0]['audioFile'])


listSenses = []
for i in listEntries:
    for j in i:
       listSenses.append(j['senses'])

listDefinitions = []
for i in listSenses:
    for j in i:
       listDefinitions.append(j['definitions'][0])

audioFile=res[0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

pprint(audioFile)



# from googletrans import Translator
#
# translator = Translator()
#
# print(translator.translate("Salom", 'en').text)