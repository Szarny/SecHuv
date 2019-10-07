import json

from flask import Flask, jsonify, request
from typing import Optional

from model.webcasepost import WebCasePost
from model.webspec import WebSpec
from model.mailcasepost import MailCasePost
from model.mailspec import MailSpec
from model.othercasepost import OtherCasePost
from model.otherspec import OtherSpec
from model.vulnerability import Vulnerability


app = Flask(__name__)

# general
@app.route("/", methods=["GET"])
def get():
    length: int = request.args.get("length", -1)


@app.route("/case", methods=["GET"])
def case_get():
    id: Optional[str] = request.args.get("id", None)

    if id is None:
        pass


@app.route("/case", methods=["DELETE"])
def case_delete():
    id: Optional[str] = request.args.get("id", None)

    if id is None:
        pass

# web
@app.route("/web/case", methods=["GET"])
def web_case_get():
    length: int = request.args.get("length", -1)


@app.route("/web/case", methods=["POST"])
def web_case_post():
    webcasepost: WebCasePost = json.loads(request.json)


@app.route("/web/valid", methods=["GET"])
def web_valid_get():
    length: int = request.args.get("length", -1)


@app.route("/web/valid", methods=["POST"])
def web_valid_post():
    webspec: WebSpec = json.loads(request.json)


@app.route("/web/check", methods=["POST"])
def web_check_post():
    webspec: WebSpec = json.loads(request.json)
    

# mail
@app.route("/mail/case", methods=["GET"])
def mail_case_get():
    length: int = request.args.get("length", -1)


@app.route("/mail/case", methods=["POST"])
def mail_case_post():
    mailcasepost: MailCasePost = json.loads(request.json)


@app.route("/mail/valid", methods=["GET"])
def mail_valid_get():
    length: int = request.args.get("length", -1)


@app.route("/mail/valid", methods=["POST"])
def mail_valid_post():
    mailspec: MailSpec = json.loads(request.json)


@app.route("/mail/check", methods=["POST"])
def mail_check_post():
    mailspec: MailSpec = json.loads(request.json)


# other
@app.route("/other/case", methods=["GET"])
def other_case_get():
    length: int = request.args.get("length", -1)


@app.route("/other/case", methods=["POST"])
def other_case_post():
    othercasepost: OtherCasePost = json.loads(request.json)


@app.route("/other/valid", methods=["GET"])
def other_valid_get():
    length: int = request.args.get("length", -1)


@app.route("/other/valid", methods=["POST"])
def other_valid_post():
    otherspec: OtherSpec = json.loads(request.json)


@app.route("/other/check", methods=["POST"])
def other_check_post():
    otherspec: OtherSpec = json.loads(request.json)


# vuln
@app.route("/vuln", methods=["GET"])
def vuln_get():
    pass


@app.route("/vuln", methods=["POST"])
def vuln_post():
    vulnerability: Vulnerability = json.loads(request.json)


@app.route("/vuln", methods=["DELETE"])
def vuln_delete():
    vulntype: Optional[str] = request.args.get("vulntype", None)

    if vulntype is None:
        pass


@app.route("/vuln/<vulntype>", methods=["GET"])
def vuln_vulntype_get(vulntype: str):
    length: int = request.args.get("length", -1)


@app.route("/vuln/<vulntype>/web", methods=["GET"])
def vuln_vulntype_web_get(vulntype: str):
    length: int = request.args.get("length", -1)


@app.route("/vuln/<vulntype>/mail", methods=["GET"])
def vuln_vulntype_mail_get(vulntype: str):
    length: int = request.args.get("length", -1)


@app.route("/vuln/<vulntype>/other", methods=["GET"])
def vuln_vulntype_other_get(vulntype: str):
    length: int = request.args.get("length", -1)


if __name__ == '__main__':
    app.run()