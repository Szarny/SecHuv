from flask import *
import requests
import json

app = Flask(__name__)
api_url = "http://localhost:8080/{}"


def get_vulns():
    vulns = json.loads(requests.get(api_url.format("vuln")).text)
    return vulns


@app.route("/")
def index():
    def get_top():
        cases = json.loads(requests.get(api_url.format(""), params={"length": 2}).text)
        return cases

    return render_template("index.html", cases=get_top(), 
                                         vulns=get_vulns())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/web")
def web():
    def get_web_cases():
        cases = json.loads(requests.get(api_url.format("web/case")).text)
        return cases

    return render_template("web.html", cases=get_web_cases(), 
                                         vulns=get_vulns())

@app.route("/mail")
def mail():
    def get_mail_cases():
        cases = json.loads(requests.get(api_url.format("mail/case")).text)
        return cases

    return render_template("mail.html", cases=get_mail_cases(), 
                                         vulns=get_vulns())

@app.route("/other")
def other():
    def get_other_cases():
        cases = json.loads(requests.get(api_url.format("other/case")).text)
        return cases

    return render_template("other.html", cases=get_other_cases(), 
                                         vulns=get_vulns())

@app.route("/vuln/<vulntype>")
def vuln(vulntype):
    def get_vuln(vulntype):
        vulns = json.loads(requests.get(api_url.format("vuln")).text)

        for vuln in vulns:
            if vuln["vulntype"] == vulntype:
                return vuln

    return render_template("vuln.html", vuln=get_vuln(vulntype),
                                        vulns=get_vulns())

                            

app.run(host="0.0.0.0", port=8000)