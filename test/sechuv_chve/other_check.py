import requests
import json

other_spec = {
    "media": "SMS",
    "metadata": "sample metadata",
    "payload": "こんにちは，http://go0gle.com です．"
}

print(json.dumps(other_spec))

response = requests.post("http://127.0.0.1:8080/other/check", 
              data=json.dumps(other_spec),
              headers={'content-type': 'application/json'})

print(response.text)