import requests
import html

URL = "https://opentdb.com/api.php"

PARAMS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(URL, params=PARAMS)
response.raise_for_status()

data = response.json()

question_data = []

for question in data["results"]:
    question["question"] = html.unescape(question["question"])
    question_data.append(question)
