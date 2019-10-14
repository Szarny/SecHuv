from typing import List
from mypy_extensions import TypedDict

from model.vulnerability import Vulnerability
from model.webspec import WebSpec

class WebCase(TypedDict):
    uuid: str
    post_date: str
    vulns: List[Vulnerability]
    spec: WebSpec
