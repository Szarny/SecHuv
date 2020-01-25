import requests
import json

web_case_post = {
    "vulntypes": ["fake_alert"],
    "spec": {
        "url": "https://www.google.com",
        "body": "body",
        "raw_body": "raw_body",
        "screenshot": ""
    }
}

# print(json.dumps(web_case_post))

response = requests.post("http://127.0.0.1:8080/web/case", 
              data=json.dumps(web_case_post),
              headers={'content-type': 'application/json'})

print(response.text)