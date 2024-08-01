import requests
import json

response = requests.get(
    "https://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow"
    )

for data in response.json()['items']:
    print(data['title'])


