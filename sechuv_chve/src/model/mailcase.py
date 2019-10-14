from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.mailspec import MailSpec

class MailCase(TypedDict):
    uuid: str
    post_date: str
    vulns: List[Vulnerability]
    spec: MailSpec