from typing import List

from vulnerability import Vulnerability
from otherspec import OtherSpec

class OtherCase:
    def __init__(self, 
                 id: str, 
                 post_date: str, 
                 vulns: List[Vulnerability], 
                 spec: OtherSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: OtherSpec = spec
