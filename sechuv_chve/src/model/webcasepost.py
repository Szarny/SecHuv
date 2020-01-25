from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.webpostspec import WebPostSpec

class WebCasePost(TypedDict):
    vulntypes: List[str]
    spec: WebPostSpec
