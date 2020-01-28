from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS
from typing import Optional, Dict, List, Tuple, Union, Any

import json
import time
import base64

from tinydb import TinyDB, Query

from model.webcase import WebCase
from model.webvalidcase import WebValidCase
from model.webcasepost import WebCasePost
from model.webspec import WebSpec
from model.webpostspec import WebPostSpec

from model.mailcase import MailCase
from model.mailvalidcase import MailValidCase
from model.mailcasepost import MailCasePost
from model.mailspec import MailSpec
from model.mailpostspec import MailPostSpec

from model.othercase import OtherCase
from model.othervalidcase import OtherValidCase
from model.othercasepost import OtherCasePost
from model.otherspec import OtherSpec
from model.otherpostspec import OtherPostSpec

from model.vulnerability import Vulnerability

import handler
import engine
import util


app: Flask = Flask(__name__)
CORS(app)


db: Dict[str, TinyDB] = {
    "web": TinyDB("/project/db/web.json"),
    "webvalid": TinyDB("/project/db/webvalid.json"),
    "mail": TinyDB("/project/db/mail.json"),
    "mailvalid": TinyDB("/project/db/mailvalid.json"),
    "other": TinyDB("/project/db/other.json"),
    "othervalid": TinyDB("/project/db/othervalid.json"),
    "vulnerability": TinyDB("/project/db/vulnerability.json"),
}


# general
@app.route("/", methods=["GET"])
def index_get():
    length: int = request.args.get("length", default=-1, type=int)
    cases: Dict[str, List[Union[WebCase, MailCase, OtherCase]]] = handler.general.index_get.handle(db=db, length=length)

    return jsonify(cases)


@app.route("/case", methods=["GET"])
def case_get():
    ok: bool
    message: str
    data: Union[Union[WebCase, MailCase, OtherCase], str]

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
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.web.web_case_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    web_case_post: WebCasePost = request.json

    web_post_spec["url"] = ":".join(web_post_spec["url"].split(":")[:2])
    
    ok, data = handler.web.web_case_post.handle(db=db, web_case_post=web_case_post)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/web/valid", methods=["GET"])
def web_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    web_valid_cases: List[WebValidCase] = handler.web.web_valid_get.handle(db=db, length=length)

    return jsonify(web_valid_cases)


@app.route("/web/valid", methods=["POST"])
def web_valid_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.web.web_valid_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    web_spec: WebSpec = request.json
    ok, data = handler.web.web_valid_post.handle(db=db, web_spec=web_spec)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/web/check", methods=["POST"])
def web_check_post():
    web_post_spec: WebPostSpec = request.json

    web_post_spec["url"] = ":".join(web_post_spec["url"].split(":")[:2])

    result: List[Dict[str, str]] = engine.web_engine.run(web_post_spec=web_post_spec)

    response = make_response(jsonify(result))

    if len(result) != 0:
        response.headers["SECHUV-Token"] = util.digisign.sign(base64.b64encode(json.dumps(web_post_spec).encode()).decode())
    
    return response
    

# mail
@app.route("/mail/case", methods=["GET"])
def mail_case_get():
    length: int = request.args.get("length", default=-1, type=int)
    mail_cases: List[MailCase] = handler.mail.mail_case_get.handle(db=db, length=length)

    return jsonify(mail_cases)


@app.route("/mail/case", methods=["POST"])
def mail_case_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.mail.mail_case_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    mail_case_post: MailCasePost = request.json
    ok, data = handler.mail.mail_case_post.handle(db=db, mail_case_post=mail_case_post)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/mail/valid", methods=["GET"])
def mail_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    mail_valid_cases: List[MailValidCase] = handler.mail.mail_valid_get.handle(db=db, length=length)

    return jsonify(mail_valid_cases)


@app.route("/mail/valid", methods=["POST"])
def mail_valid_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.mail.mail_valid_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    mail_spec: MailSpec = request.json
    ok, data = handler.mail.mail_valid_post.handle(db=db, mail_spec=mail_spec)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/mail/check", methods=["POST"])
def mail_check_post():
    mail_post_spec: MailPostSpec = request.json

    result: List[Dict[str, str]] = engine.mail_engine.run(mail_post_spec=mail_post_spec)

    response = make_response(jsonify(result))

    if len(result) != 0:
        response.headers["SECHUV-Token"] = util.digisign.sign(base64.b64encode(json.dumps(mail_post_spec).encode()).decode())
    
    return response



# other
@app.route("/other/case", methods=["GET"])
def other_case_get():
    length: int = request.args.get("length", default=-1, type=int)
    other_cases: List[OtherCase] = handler.other.other_case_get.handle(db=db, length=length)

    return jsonify(other_cases)


@app.route("/other/case", methods=["POST"])
def other_case_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.other.other_case_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    other_case_post: OtherCasePost = request.json
    ok, data = handler.other.other_case_post.handle(db=db, other_case_post=other_case_post)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/other/valid", methods=["GET"])
def other_valid_get():
    length: int = request.args.get("length", default=-1, type=int)
    other_valid_cases: List[OtherValidCase] = handler.other.other_valid_get.handle(db=db, length=length)

    return jsonify(other_valid_cases)


@app.route("/other/valid", methods=["POST"])
def other_valid_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.other.other_valid_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    other_spec: OtherSpec = request.json
    ok, data = handler.other.other_valid_post.handle(db=db, other_spec=other_spec)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


@app.route("/other/check", methods=["POST"])
def other_check_post():
    other_post_spec: OtherPostSpec = request.json

    result: List[Dict[str, str]] = engine.other_engine.run(other_post_spec=other_post_spec)

    response = make_response(jsonify(result))

    if len(result) != 0:
        response.headers["SECHUV-Token"] = util.digisign.sign(base64.b64encode(json.dumps(other_post_spec).encode()).decode())
    
    return response


@app.route("/vuln", methods=["GET"])
def vuln_get():
    vulnerabilities: List[Vulnerability] = handler.vuln.vuln_get.handle(db=db)

    return jsonify(vulnerabilities)


@app.route("/vuln", methods=["POST"])
def vuln_post():
    ok: bool
    data: Dict[str, str]

    # 未実装
    ok = handler.vuln.vuln_post.validation(post_data=request.json)
    if not ok:
        abort(400, {"message": "Posted value is invalid."})

    vulnerability: Vulnerability = request.json
    ok, data = handler.vuln.vuln_post.handle(db=db, vulnerability=vulnerability)
    if not ok:
        abort(500, {"message": "Server error."})

    return jsonify(data)


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

    data: Dict[str, Any] = handler.vuln.vuln_vulntype_get.handle(db=db, length=length, vulntype=vulntype)

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
    time.sleep(1)
    app.run(host="0.0.0.0", port=8080)