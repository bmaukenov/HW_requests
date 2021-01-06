import os
import requests
IAM_TOKEN = 't1.9euelZrPkJ2dlcuYlcyejJLHicjOku3rnpWazZDNio6dzMaVz5bKl8-SkY_l8_dbDyoA-u9vICsY_d3z9xs-JwD6728gKxj9.Z8fypFvMaBAQB_TMIC0q0mlzsH4azsCiWC91YdmkAYwsfAnm3HxmALifnd271uLgePzlx8IXlzA6k3qrP_hkDw'
FOLDER_ID = os.getenv('b1gitleg3ur0o1bmovtm')
print(IAM_TOKEN)
def translate(texts):
    url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
        'Content-Type': 'application/json',
    }

    params = {
  "sourceLanguageCode": "fr",
  "targetLanguageCode": "ru",
  "format": "PLAIN_TEXT",
  "texts": [
    texts
  ],
  "folderId": FOLDER_ID,

    }
    data = {
        'folder_id': FOLDER_ID,
        'texts': texts,
        'targetLanguageCode': 'ru'
    }
    response = requests.post(url, headers=headers, params = params, json=data)
    response.raise_for_status()
    data = response.json()
    return data.get('translations', [])

    with open(result_file_path, "w") as result_file:
        result_file.write(result)





def yandex_download():
    URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    params = {"path" : "6 января.txt", "overwrite" : "true"}

    headers = {"Authorization" : "OAuth AgAAAAAZdNVWAAbNc6C12UBVhEYPoMwFNBzlJXI"}

    req = requests.get(URL, params = params, headers = headers)
    trial = req.json()["href"]
    files = {'file': open('/Users/beksultan_maukenov/Desktop/py-homework-basic-files/3.2.http.requests/FRtest.txt', 'rb')}    
    req_2 = requests.put(trial, files = files)




if __name__ == '__main__':
    initial_file_path = "/Users/beksultan_maukenov/Desktop/py-homework-basic-files/3.2.http.requests/FRtest.txt"
    result_file_path = "/Users/beksultan_maukenov/Desktop/result.txt"


    with open(initial_file_path) as initial_file:
        texts = initial_file.read()
        result = translate(texts)
        yandex_download(result)

