from typing import List

from model.vulnerability import Vulnerability
from model.otherspec import OtherSpec

class OtherCase:
    def __init__(self, 
                 uuid: str, 
                 post_date: str, 
                 vulns: List[Vulnerability], 
                 spec: OtherSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: OtherSpec = spec
