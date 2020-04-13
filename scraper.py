import requests
import json

from time import time


def scraper():
    """Extract data from the official state site api."""

    endpoint_url = 'https://coronavirus.guanajuato.gob.mx/infectados.json'

    req = requests.get(endpoint_url)
    req.raise_for_status()
    data = req.json()

    parsed_data = {
        'timestamp': time(),
        'resumen': data['casos'],
        'estados': {}
    }

    for name, values in data['listado'].items():
        parsed_data['estados'][name] = {
            k: v for i in values for k, v in i.items()
        }

    return parsed_data


if __name__ == "__main__":
    data = scraper()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
