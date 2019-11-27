from flask import *
import requests
import json

app = Flask(__name__)
app.data = {}
api_url = "http://api_server:8080/{}"


def get_vulns():
    vulns = json.loads(requests.get(api_url.format("vuln")).text)
    return vulns


@app.route("/")
def index():
    def get_top():
        cases = json.loads(requests.get(api_url.format(""), params={"length": 10}).text)
        return cases

    return render_template("index.html", cases=get_top(), 
                                         vulns=app.data["vulns"])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/web")
def web():
    def get_web_cases():
        cases = json.loads(requests.get(api_url.format("web/case")).text)
        return cases

    return render_template("web.html", cases=get_web_cases(), 
                                         vulns=app.data["vulns"])


@app.route("/web/<uuid>")
def web_case(uuid):
    def get_web_case(uuid):
        case = json.loads(requests.get(api_url.format("case"), params={"uuid": uuid, "kind": "web", "is_valid": "false"}).text)
        return case

    return render_template("webcase.html", case=get_web_case(uuid), 
                                         vulns=app.data["vulns"])


@app.route("/mail")
def mail():
    def get_mail_cases():
        cases = json.loads(requests.get(api_url.format("mail/case")).text)
        return cases

    return render_template("mail.html", cases=get_mail_cases(), 
                                         vulns=app.data["vulns"])


@app.route("/mail/<uuid>")
def mail_case(uuid):
    def get_mail_case(uuid):
        case = json.loads(requests.get(api_url.format("case"), params={"uuid": uuid, "kind": "mail", "is_valid": "false"}).text)
        return case

    return render_template("mailcase.html", case=get_mail_case(uuid), 
                                         vulns=app.data["vulns"])


@app.route("/other")
def other():
    def get_other_cases():
        cases = json.loads(requests.get(api_url.format("other/case")).text)
        return cases

    return render_template("other.html", cases=get_other_cases(), 
                                         vulns=app.data["vulns"])


@app.route("/other/<uuid>")
def other_case(uuid):
    def get_other_case(uuid):
        case = json.loads(requests.get(api_url.format("case"), params={"uuid": uuid, "kind": "other", "is_valid": "false"}).text)
        return case

    return render_template("othercase.html", case=get_other_case(uuid), 
                                         vulns=app.data["vulns"])


@app.route("/vuln/<vulntype>")
def vuln_cases(vulntype):
    def get_vuln(vulntype):
        vulns = json.loads(requests.get(api_url.format("vuln")).text)

        for vuln in vulns:
            if vuln["vulntype"] == vulntype:
                return vuln

    def get_cases(vulntype):
        cases = json.loads(requests.get(api_url.format("vuln/{}".format(vulntype))).text)
        return cases

    return render_template("vulncases.html", vuln=get_vuln(vulntype),
                                             vulns=app.data["vulns"],
                                             cases=get_cases(vulntype))

                            
app.data["vulns"] = get_vulns()
app.run(host="0.0.0.0", port=8000)