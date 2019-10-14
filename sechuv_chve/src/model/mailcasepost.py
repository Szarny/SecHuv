from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.mailspec import MailSpec

class MailCasePost(TypedDict):
    vulns: List[Vulnerability]
    spec: MailSpec