from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.webspec import WebSpec

class WebCasePost(TypedDict):
    vulns: List[Vulnerability]
    spec: WebSpec
