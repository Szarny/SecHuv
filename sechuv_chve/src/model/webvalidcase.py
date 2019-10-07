from typing import List

from .webspec import WebSpec

class WebCase:
    def __init__(self, 
                 id: str, 
                 post_date: str, 
                 spec: WebSpec) -> None:
        self.id: str = id
        self.post_date: str = post_date
        self.spec: WebSpec = spec
