#!/usr/bin/env python3
import datetime
import requests


name = 'Serhii Korobkov'
date = str(datetime.date.today())
url = 'https://baconipsum.com/api'
filename = 'result.txt'


def count_pancetta(input: list) -> int:
    return len(list(filter(lambda x: 'pancetta' in x.lower(), input)))


paragraphs = input("Enter number of paragraphs (default 5): ")
if paragraphs:
    paragraphs = int(paragraphs)
else:
    paragraphs = 5

params = {'type': 'all-meat', 'paras': paragraphs, 'format': 'json'}
r = requests.get(url, params)
if r.status_code == 200:
    resp = r.json()
    if type(resp) is list:
        # resp.reverse()
        resp = resp[::-1]
        pancettas = count_pancetta(resp)
        with open(filename, 'w') as file:
            file.write('{} {} {}\n'.format(name, date, pancettas))
            file.write('\n'.join(resp))
