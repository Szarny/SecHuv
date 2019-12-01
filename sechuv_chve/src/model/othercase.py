from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.otherspec import OtherSpec

class OtherCase(TypedDict):
    uuid: str
    post_date: str
    vulntypes: List[str]
    spec: OtherSpec
