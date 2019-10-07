from typing import List

from .otherspec import OtherSpec

class OtherValidCase:
    def __init__(self, 
                 uuid: str, 
                 post_date: str,
                 spec: OtherSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.spec: OtherSpec = spec
