import requests


def translate(q: str, source: str = 'en', target: str = 'pt') -> str:
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = f"target={target}&q={q}&target={target}" #"source=en&q=Testing a Text!&target=pt"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "f2bd7731d9msh1c5708c818c9f2ep174350jsnbb8010b6b1fa",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text

print(translate('Andas Ancestral Tomb'))
