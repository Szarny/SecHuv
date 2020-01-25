from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.mailpostspec import MailPostSpec

class MailCasePost(TypedDict):
    vulntypes: List[str]
    spec: MailPostSpec