from typing import List
from mypy_extensions import TypedDict

from .vulnerability import Vulnerability
from .mailspec import MailSpec

class MailCase(TypedDict):
    uuid: str
    post_date: str
    vulntypes: List[str]
    spec: MailSpec