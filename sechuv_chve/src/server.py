import json

from flask import Flask, jsonify, request, abort
from typing import Optional, Dict, List, Tuple, Union

from tinydb import TinyDB, Query

from model.case import Case

from model.webcase import WebCase
from model.webvalidcase import WebValidCase
from model.webcasepost import WebCasePost
from model.webspec import WebSpec

from model.mailcase import MailCase
from model.mailvalidcase import MailValidCase
from model.mailcasepost import MailCasePost
from model.mailspec import MailSpec

from model.othercase import OtherCase
from model.othervalidcase import OtherValidCase
from model.othercasepost import OtherCasePost
from model.otherspec import OtherSpec

from model.vulnerability import Vulnerability

import handler


app: Flask = Flask(__name__)


db: Dict[str, TinyDB] = {
    "web": TinyDB("db/web.json"),
    "webvalid": TinyDB("db/webvalid.json"),
    "mail": TinyDB("db/mail.json"),
    "mailvalid": TinyDB("db/mailvalid.json"),
    "other": TinyDB("db/other.json"),
    "othervalid": TinyDB("db/othervalid.json"),
    "vulnerability": TinyDB("db/vulnerability.json"),
}


# general
@app.route("/", methods=["GET"])
def index_get():
    length: int = request.args.get("length", default=-1, type=int)
    cases: Dict[str, List[Case]] = handler.general.index_get.handle(db=db, length=length)

    return jsonify(cases)


@app.route("/case", methods=["GET"])
def case_get():
    ok: bool
    message: str
    data: Union[Case, str]

    uuid: Optional[str] = request.args.get("uuid", None)
    kind: Optional[str] = request.args.get("kind", None)
    is_valid: Optional[str] = request.args.get("is_valid", None)

    ok, message = handler.general.case_get.validation(uuid=uuid, kind=kind, is_valid=is_valid)
    if not ok:
        abort(400, {"message": message})

    _is_valid: bool = is_valid == "true"

    ok, data = handler.general.case_get.handle(db=db, uuid=uuid, kind=kind, is_valid=_is_valid)
    if not ok:
        abort(400, {"message": data})

    return jsonify(data)


@app.route("/case", methods=["DELETE"])
def case_delete():
    ok: bool
    message: str
    data: str

    uuid: Optional[str] = request.args.get("uuid", None)
    kind: Optional[str] = request.args.get("kind", None)
    is_valid: Optional[str] = request.args.get("is_valid", None)

    ok, message = handler.general.case_delete.validation(uuid=uuid, kind=kind, is_valid=is_valid)
    if not ok:
        abort(400, {"message": message})

    _is_valid: bool = is_valid == "true"

    ok, data = handler.general.case_delete.handle(db=db, uuid=uuid, kind=kind, is_valid=_is_valid)
    if not ok:
        abort(400, {"message": data})

    return jsonify({"uuid": uuid})


# web
@app.route("/web/case", methods=["GET"])
def web_case_get():
    length: int = request.args.get("length", default=-1, type=int)
    web_cases: List[WebCase] = handler.web.web_case_get.handle(db=db, length=length)

    return jsonify(web_cases)


@app.route("/web/case", methods=["POST"])
def web_case_post():
    web_case_post: WebCasePost = json.loads(request.json)


@app.route("/web/valid", methods=["GET"])
def web_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    web_valid_cases: List[WebValidCase] = handler.web.web_valid_get.handle(db=db, length=length)

    return jsonify(web_valid_cases)

@app.route("/web/valid", methods=["POST"])
def web_valid_post():
    web_spec: WebSpec = json.loads(request.json)


@app.route("/web/check", methods=["POST"])
def web_check_post():
    web_spec: WebSpec = json.loads(request.json)
    

# mail
@app.route("/mail/case", methods=["GET"])
def mail_case_get():
    length: int = request.args.get("length", default=-1, type=int)
    mail_cases: List[MailCase] = handler.mail.mail_case_get.handle(db=db, length=length)

    return jsonify(mail_cases)


@app.route("/mail/case", methods=["POST"])
def mail_case_post():
    mail_case_post: MailCasePost = json.loads(request.json)


@app.route("/mail/valid", methods=["GET"])
def mail_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    mail_valid_cases: List[MailValidCase] = handler.mail.mail_valid_get.handle(db=db, length=length)

    return jsonify(mail_valid_cases)


@app.route("/mail/valid", methods=["POST"])
def mail_valid_post():
    mail_spec: MailSpec = json.loads(request.json)


@app.route("/mail/check", methods=["POST"])
def mail_check_post():
    mail_spec: MailSpec = json.loads(request.json)


# other
@app.route("/other/case", methods=["GET"])
def other_case_get():
    length: int = request.args.get("length", default=-1, type=int)
    other_cases: List[OtherCase] = handler.other.other_case_get.handle(db=db, length=length)

    return jsonify(other_cases)


@app.route("/other/case", methods=["POST"])
def other_case_post():
    other_case_post: OtherCasePost = json.loads(request.json)


@app.route("/other/valid", methods=["GET"])
def other_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    other_valid_cases: List[OtherValidCase] = handler.other.other_valid_get.handle(db=db, length=length)

    return jsonify(other_valid_cases)


@app.route("/other/valid", methods=["POST"])
def other_valid_post():
    other_spec: OtherSpec = json.loads(request.json)


@app.route("/other/check", methods=["POST"])
def other_check_post():
    other_spec: OtherSpec = json.loads(request.json)


# vuln
@app.route("/vuln", methods=["GET"])
def vuln_get():
    vulnerabilities: List[Vulnerability] = handler.vuln.vuln_get.handle(db=db)

    return jsonify(vulnerabilities)


@app.route("/vuln", methods=["POST"])
def vuln_post():
    vulnerability: Vulnerability = json.loads(request.json)


@app.route("/vuln", methods=["DELETE"])
def vuln_delete():
    vulntype: Optional[str] = request.args.get("vulntype", None)

    ok, message = handler.vuln.vuln_delete.validation(vulntype=vulntype)
    if not ok:
        abort(400, {"message": message})

    ok, data = handler.vuln.vuln_delete.handle(db=db, vulntype=vulntype)
    if not ok:
        abort(400, {"message": data})

    return jsonify({"vulntype": vulntype})


@app.route("/vuln/<vulntype>", methods=["GET"])
def vuln_vulntype_get(vulntype: str):
    length: int = request.args.get("length", default=-1, type=int)

    ok: bool
    message: str

    ok, message = handler.vuln.vuln_vulntype_get.validation(db=db, vulntype=vulntype)
    if not ok:
        abort(400, {"message": message})

    data: Dict[str, Union[Vulnerability, Dict[str, List[Case]]]] = handler.vuln.vuln_vulntype_get.handle(db=db, length=length, vulntype=vulntype)

    return jsonify(data)

@app.route("/vuln/<vulntype>/web", methods=["GET"])
def vuln_vulntype_web_get(vulntype: str):
    length: int = request.args.get("length", default=-1, type=int)

    ok: bool
    message: str

    ok, message = handler.vuln.vuln_vulntype_web_get.validation(db=db, vulntype=vulntype)
    if not ok:
        abort(400, {"message": message})

    data: Dict[str, Union[Vulnerability, List[WebCase]]] = handler.vuln.vuln_vulntype_web_get.handle(db=db, length=length, vulntype=vulntype)

    return jsonify(data)


@app.route("/vuln/<vulntype>/mail", methods=["GET"])
def vuln_vulntype_mail_get(vulntype: str):
    length: int = request.args.get("length", default=-1, type=int)

    ok: bool
    message: str

    ok, message = handler.vuln.vuln_vulntype_mail_get.validation(db=db, vulntype=vulntype)
    if not ok:
        abort(400, {"message": message})

    data: Dict[str, Union[Vulnerability, List[MailCase]]] = handler.vuln.vuln_vulntype_mail_get.handle(db=db, length=length, vulntype=vulntype)

    return jsonify(data)

@app.route("/vuln/<vulntype>/other", methods=["GET"])
def vuln_vulntype_other_get(vulntype: str):
    length: int = request.args.get("length", default=-1, type=int)

    ok: bool
    message: str

    ok, message = handler.vuln.vuln_vulntype_other_get.validation(db=db, vulntype=vulntype)
    if not ok:
        abort(400, {"message": message})
    
    data: Dict[str, Union[Vulnerability, List[OtherCase]]] = handler.vuln.vuln_vulntype_other_get.handle(db=db, length=length, vulntype=vulntype)

    return jsonify(data)


@app.errorhandler(400)
@app.errorhandler(500)
def error_handler(error):
    response = jsonify({ 'message': error.description['message']})
    return response, error.code


if __name__ == '__main__':
    app.run()