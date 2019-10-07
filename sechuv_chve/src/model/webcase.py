from typing import List

from .vulnerability import Vulnerability
from .webspec import WebSpec

class WebCase:
    def __init__(self, 
                 uuid: str, 
                 post_date: str, 
                 vulns: List[Vulnerability], 
                 spec: WebSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: WebSpec = spec
