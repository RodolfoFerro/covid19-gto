import requests
import json

from time import time
from hashlib import md5


def scraper(old_checksum=None):
    """Extract data from the official state site api."""

    endpoint_url = 'https://coronavirus.guanajuato.gob.mx/infectados.json'

    req = requests.get(endpoint_url)
    req.raise_for_status()
    data = req.json()

    new_checksum = md5(req.content).hexdigest()

    if new_checksum == old_checksum:
        return {}

    parsed_data = {
        'checksum': new_checksum,
        'timestamp': time(),
        'resumen': data['casos'],
        'estados': {}
    }

    for name, values in data['listado'].items():
        parsed_data['estados'][name] = {
            k: v for i in values for k, v in i.items()
        }

    return parsed_data


def run_and_save(filename='data/data.json',
                 checksum_filename='data/data_checksum.txt'):
    with open(checksum_filename, 'r') as f:
        old_checksum = f.read()

    data = scraper(old_checksum=old_checksum)

    if not data:
        return

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(checksum_filename, 'w') as f:
        f.write(data['checksum'])


if __name__ == "__main__":
    run_and_save()
