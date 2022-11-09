import requests
tafsir="uzb-muhammadsodikmu"
sura=1
oyat=4
URL_SURA=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
URL_OYAT = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

response_sura=requests.get(URL_SURA)
response_oyat=requests.get(URL_OYAT)

list_oyat=response_sura.json()['chapter']

for i in list_oyat:

    print(f"{i['verse']} oyat")
    print(i['text'])
