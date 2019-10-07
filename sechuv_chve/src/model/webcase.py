from typing import List

from .vulnerability import Vulnerability
from .webspec import WebSpec

class WebCase:
    def __init__(self, 
                 id: str, 
                 post_date: str, 
                 vulns: List[Vulnerability], 
                 spec: WebSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.vulns: List[Vulnerability] = vulns
        self.spec: WebSpec = spec
