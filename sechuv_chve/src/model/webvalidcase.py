from typing import List

from model.webspec import WebSpec

class WebValidCase:
    def __init__(self, 
                 uuid: str, 
                 post_date: str, 
                 spec: WebSpec) -> None:
        self.uuid: str = uuid
        self.post_date: str = post_date
        self.spec: WebSpec = spec
