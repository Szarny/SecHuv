from typing import List
from mypy_extensions import TypedDict

from .vulnerability import Vulnerability
from .mailspec import MailSpec

class MailCasePost(TypedDict):
    vulntypes: List[str]
    spec: MailSpec