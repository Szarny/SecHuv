import requests
import json

mail_spec = {
    "from_addr": "hogefuga@http://go0gle.com",
    "spf_status": "pass",
    "dkim_status": "none",
    "is_html": True,
    "subject": "string",
    "body": "string",
    "raw_body": "こんにちは，http://google-login.com です．",
    "webcase_ptrs": []
}

print(json.dumps(mail_spec))

response = requests.post("http://127.0.0.1:8080/mail/check", 
              data=json.dumps(mail_spec),
              headers={'content-type': 'application/json'})

print(response.text)