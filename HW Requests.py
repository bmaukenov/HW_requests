import requests


def translate(initial_file_path, final_file_path, to_lang):
    IAM_TOKEN = ''
    FOLDER_ID = ''
    url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
    with open(initial_file_path) as file:
        texts = file.read()
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'folder_id': FOLDER_ID,
        'texts': texts,
        'targetLanguageCode': to_lang
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    data = response.json()
    with open(final_file_path, "w") as file:
        file.write(str(data.get('translations', [])[0]["text"]))
    return final_file_path


def yandex_disk_download(file_path):
    file_name = file_path.split("/")[-1] + ".txt"
    URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    params = {"path": file_name, "overwrite": "true"}
    headers = {"Authorization": "OAuth AgAAAAAZdNVWAAbNc6C12UBVhEYPoMwFNBzlJXI"}
    first_req = requests.get(URL, params=params, headers=headers)
    second_req = first_req.json()
    download_link = second_req["href"]
    file = {"file": open(file_path)}
    downloading = requests.put(download_link, files=file)
    downloading.raise_for_status()
    if str(downloading) == "<Response [201]>":
        print("Done")
    else:
        print("There are some technical problems, sorry")


if __name__ == '__main__':
    initial_file_path = '/Users/beksultan_maukenov/Desktop/py-homework-basic-files/3.2.http.requests/FRtest.txt'
    final_file_path = '/Users/beksultan_maukenov/Desktop/py-homework-basic-files/3.2.http.requests/Result_FRtest.txt'
    to_lang = "ru"
    file_path = translate(initial_file_path, final_file_path, to_lang)
    yandex_disk_download(file_path)
