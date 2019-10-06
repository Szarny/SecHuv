from typing import List

from otherspec import OtherSpec

class OtherValidCase:
    def __init__(self, 
                 id: str, 
                 post_date: str,
                 spec: OtherSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.spec: OtherSpec = spec
