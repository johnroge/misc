#!/usr/bin/env python3

import requests
import collections

search = 'capital'
url = 'http://movie_database.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)

print(resp.text)


