from typing import List
from mypy_extensions import TypedDict

from model.webspec import WebSpec

class WebValidCase(TypedDict):
    uuid: str
    post_date: str
    spec: WebSpec
