import requests
import json

web_spec = {
    "url": "http://www.go0gle.com",
    "body": "body",
    "raw_body": "raw_body",
    "screenshot": "screenshot"
}

print(json.dumps(web_spec))

response = requests.post("http://127.0.0.1:8080/web/check", 
              data=json.dumps(web_spec),
              headers={'content-type': 'application/json'})

print(response.text)