from typing import List
from mypy_extensions import TypedDict

from .mailspec import MailSpec

class MailValidCase(TypedDict):
    uuid: str
    post_date: str
    spec: MailSpec