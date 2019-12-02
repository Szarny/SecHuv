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
from model.vulnerability import Vulnerability


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
        # self.attach_file_list = {}

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
            # else:
            #     print(part)
            #     self.attach_file_list.append({
            #         "name": attach_fname,
            #         "data": part.get_payload()
            #     })

    def parse_from_addr(self):
        self.from_addr = re.match("^.*\<(.+)\>.*$", self.from_addr).group(1)

    def parse_authentication_result(self):
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
            "is_html": False,
            "body": None,
            "raw_body": self.body,
            "webcase_ptrs": []
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

    mail = MailParser("input/example.eml")

if __name__ == '__main__':
    main()