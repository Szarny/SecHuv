import requests
import json

vuln1 = {
    "vulntype": "vuln1",
    "description": "vuln type one"
}

vuln2 = {
    "vulntype": "vuln2",
    "description": "vuln type two"
}

web_case_post = {
    "vulntypes": [
        "vuln1", "vuln2"
    ],
    "spec": {
        "url": "http://foo.com",
        "body": "<h1>hello!</h1>",
        "raw_body": "hello!",
        "screenshot": "image"
    }
}

mail_case_post = {
    "vulntypes": [
        "vuln1", "vuln2"
    ],
    "spec": {
        "from_addr": "a@b.c",
        "spf_status": "pass",
        "dkim_status": "none",
        "is_html": True,
        "subject": "string",
        "body": "string",
        "raw_body": "string",
        "webcase_ptrs": []
    }
}

other_case_post = {
    "vulntypes": [
        "vuln1", "vuln2"
    ],
    "spec": {
        "media": "string",
        "metadata": "string",
        "payload": "string"
    }
}

web_spec = {
    "url": "http://foo.com",
    "body": "<h1>hello!</h1>",
    "raw_body": "hello!",
    "screenshot": "image"
}

mail_spec = {
    "from_addr": "a@b.c",
    "spf_status": "pass",
    "dkim_status": "none",
    "is_html": True,
    "subject": "string",
    "body": "string",
    "raw_body": "string",
    "webcase_ptrs": []
}

other_spec = {
    "media": "string",
    "metadata": "string",
    "payload": "string"
}

requests.post("http://127.0.0.1:8080/vuln", 
              data=json.dumps(vuln1),
              headers={'content-type': 'application/json'})

requests.post("http://127.0.0.1:8080/vuln", 
              data=json.dumps(vuln2),
              headers={'content-type': 'application/json'})

requests.post("http://127.0.0.1:8080/web/case", 
              data=json.dumps(web_case_post),
              headers={'content-type': 'application/json'})
requests.post("http://127.0.0.1:8080/mail/case", 
              data=json.dumps(mail_case_post),
              headers={'content-type': 'application/json'})
requests.post("http://127.0.0.1:8080/other/case", 
              data=json.dumps(other_case_post),
              headers={'content-type': 'application/json'})

# requests.post("http://127.0.0.1:8080/web/valid", 
#               data=json.dumps(web_spec),
#               headers={'content-type': 'application/json'})
# requests.post("http://127.0.0.1:8080/mail/valid", 
#               data=json.dumps(mail_spec),
#               headers={'content-type': 'application/json'})
# requests.post("http://127.0.0.1:8080/other/valid", 
#               data=json.dumps(other_spec),
#               headers={'content-type': 'application/json'})