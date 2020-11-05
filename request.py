import requests

url = 'http/localhost:5000/results'
r = requests.post(url, json={'input text': 'I love machine learning'})

print(r.json())
