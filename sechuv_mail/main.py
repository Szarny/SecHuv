import requests
import json

from typing import List, Tuple, Optional

import glob
import re
import email
from email.header import decode_header

from util import console

from model.mailcase import MailCase
from model.mailcasepost import MailCasePost
from model.mailspec import MailSpec
from model.mailvalidcase import MailValidCase
from model.mailpostspec import MailPostSpec
from model.vulnerability import Vulnerability


check_url: str = "http://localhost:8080/mail/check"
post_url: str = "http://localhost:8080/mail/case"

class MailParser(object):
    def __init__(self, mail_file_path):
        self.mail_file_path = mail_file_path
        with open(mail_file_path, 'r') as email_file:
            self.email_message = email.message_from_string(email_file.read())
        self.subject = None
        self.from_addr = None
        self.auth_result = None
        self.spf_status = None
        self.dkim_status = None
        self.body = ""
        self.attach_file_list = []

        self.parse()


    def parse(self):
        self.subject = self.get_decoded_header("Subject")
        self.from_addr = self.get_decoded_header("From")
        self.parse_from_addr()
        
        self.auth_result = self.get_decoded_header("Authentication-Results")
        self.parse_authentication_result()

        for part in self.email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue

            attach_fname = part.get_filename()
            if not attach_fname:
                charset = str(part.get_content_charset())
                if charset:
                    self.body += part.get_payload(decode=True).decode(charset, errors="replace")
                else:
                    self.body += part.get_payload(decode=True)
            else:
                self.attach_file_list.append({
                    "name": decode_header(attach_fname)[0][0],
                    "data": part.get_payload(decode=True)
                })

    def parse_from_addr(self):
        self.from_addr = re.match("^.*\<(.+)\>.*$", self.from_addr).group(1)

    def parse_authentication_result(self):
        if self.auth_result is None:
            self.spf_status = "unknown"
            self.dkim_status = "unknown"
            return

        for row in self.auth_result.split("\n"):
            if self.spf_status is None and "spf=" in row:
                self.spf_status = re.match("^.*spf=([a-z]+).*$", row).group(1)

            if self.dkim_status is None and "dkim=" in row:
                self.dkim_status = re.match("^.*dkim=([a-z]+).*$", row).group(1)


    def get_decoded_header(self, key_name):
        ret = ""

        raw_obj = self.email_message.get(key_name)
        if raw_obj is None:
            return None
        for fragment, encoding in decode_header(raw_obj):
            if not hasattr(fragment, "decode"):
                ret += fragment
                continue
            if encoding:
                ret += fragment.decode(encoding)
            else:
                ret += fragment.decode("UTF-8")
        return ret

    
    def summarize(self):
        return {
            "subject": self.subject,
            "from_addr": self.from_addr,
            "spf_status": self.spf_status,
            "dkim_status": self.dkim_status,
            "body": self.body,
            "attach_files": [attach_file["name"] for attach_file in self.attach_file_list]
        }


def show_welcome() -> None:
    print("""
 ____            _   _               __  __       _ _
/ ___|  ___  ___| | | |_   ___   ___|  \/  | __ _(_) |
\___ \ / _ \/ __| |_| | | | \ \ / (_) |\/| |/ _` | | |
 ___) |  __/ (__|  _  | |_| |\ V / _| |  | | (_| | | |
|____/ \___|\___|_| |_|\__,_| \_/ (_)_|  |_|\__,_|_|_|
=======================================================
""")
    console.info("SecHuv:Mailを起動しました")


def main() -> None:
    show_welcome()

    mail = MailParser(input("emlファイルのパスを入力してください >> "))

    for attach_file in mail.attach_file_list:
        with open("attachment/{}".format(attach_file["name"].decode()), "wb") as f:
            f.write(attach_file["data"])

    console.info("メールを読み込みました。検査を行います。")
    print()

    mail_post_spec: MailPostSpec = {
        "from_addr": mail.from_addr,
        "spf_status": mail.spf_status,
        "dkim_status": mail.dkim_status,
        "subject": mail.subject,
        "body": mail.body,
        "attach_files": [attach_file["name"] for attach_file in mail.attach_file_list]
    }

    headers = {"Content-Type" : "application/json"}
    data = json.dumps(mail_post_spec)
    response = requests.post(check_url, data=data, headers=headers)

    if response.status_code != 200:
        console.error("メールの検査中にエラーが発生しました")
        print(response.text)
        exit()

    vulns = json.loads(response.text)

    if len(vulns) == 0:
        console.info("本メールから、人的脆弱性を突いた攻撃と思わしき兆候は検出されませんでした。")
        exit()

    vulntypes: List[str] = []
    console.warn("本メールから、以下の人的脆弱性を突いた攻撃と思わしき兆候が検出されました。")

    for vuln in vulns:
        console.warn(f"{vuln['vulntype']} - 詳しくはこちら:http://localhost:8000/vuln/{vuln['vulntype']}")
        vulntypes.append(vuln["vulntype"])
    
    print()
    is_report = console.ask("本メールを報告しますか？")

    if "y" not in is_report and "はい" not in is_report:
        console.info("SecHuv:Mailを終了します")

    mail_case_post: MailCasePost = {
        "vulntypes": vulntypes,
        "spec": mail_post_spec
    }

    headers = {
        "Content-Type" : "application/json",
        "SECHUV-Token": response.headers.get("SECHUV-Token")
    }
    data = json.dumps(mail_case_post)
    response = requests.post(post_url, data=data, headers=headers)

    if response.status_code != 200:
        console.error("報告中にエラーが発生しました")
        print(response.text)
        exit()

    console.info("報告が完了しました。報告された情報は以下のURLで閲覧できます。")
    console.info(f"http://localhost:8000/mail/{json.loads(response.text)['uuid']}")

if __name__ == '__main__':
    main()