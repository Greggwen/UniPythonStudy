#!/bin/python3


import requests
import json

if __name__ == "__main__":
    target = 'https://unsplash.com/napi/collections/3330448/photos?page=3&per_page=10&order_by=latest&share_key=039a27cbd24691f95ac32fe494ce28f8'

    req = requests.get(target)

    data = json.loads(req.text)

    for item in data:
        print(item['id'], item['links']['download'])
        r = requests.get(item['links']['download'], stream=True)
        with open('./images/' + item['id'] + '.jpeg', 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)