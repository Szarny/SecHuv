from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.otherspec import OtherSpec

class OtherCasePost(TypedDict):
    vulntypes: List[str]
    spec: OtherSpec
