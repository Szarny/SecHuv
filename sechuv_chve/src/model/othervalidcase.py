from typing import List
from mypy_extensions import TypedDict

from model.otherspec import OtherSpec

class OtherValidCase(TypedDict):
    uuid: str
    post_date: str
    spec: OtherSpec
