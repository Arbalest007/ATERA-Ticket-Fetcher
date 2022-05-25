from asyncio.windows_events import NULL
import requests
import json

#Update from Admin Panel when running script
api_key = 0

session = requests.Session()
session.headers.update({'X-API-KEY': api_key})

parameters = {'itemsInPage': 50}

response = session.get('https://app.atera.com/api/v3/tickets', params=parameters)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())