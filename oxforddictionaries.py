import requests

app_id = "7cb38fcc"
app_key = 'f2d92f92a152cc7a33e4531636544add'

language = 'en-gb'


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    res = r.json()

    if "error" in res.keys():
        return False

    output = {}
    res = r.json()['results']

    listLexicalEntries = []

    for i in res:
        listLexicalEntries.append(i['lexicalEntries'])

    listEntries = []
    for i in listLexicalEntries:
        for j in i:
            listEntries.append(j['entries'])

    listSenses = []
    for i in listEntries:
        for j in i:
            listSenses.append(j['senses'])

    listDefinitions = []
    for i in listSenses:
        for j in i:
            listDefinitions.append(f"✅ {j['definitions'][0]}")

    output['definitions'] = "\n".join(listDefinitions)
    if res[0]['lexicalEntries'][0]['entries'][0].get('pronunciations'):
        if res[0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
            audioFile = res[0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
            output['audio'] = audioFile



    return output