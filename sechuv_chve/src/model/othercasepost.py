from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.otherpostspec import OtherPostSpec

class OtherCasePost(TypedDict):
    vulntypes: List[str]
    spec: OtherPostSpec
