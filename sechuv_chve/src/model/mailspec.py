from typing import Optional, List

class MailSpec:
    def __init__(self, 
                 from_addr: str,
                 spf_status: str,
                 dkim_status: str,
                 is_html: bool,
                 subject: str,
                 body: str,
                 raw_body: str,
                 webcase_ptrs: Optional[List[str]]) -> None:
        self.from_addr: str = from_addr
        self.spf_status: str = spf_status
        self.dkim_status: str = dkim_status
        self.is_html: bool = is_html
        self.subject: str = subject
        self.body: Optional[str] = body
        self.raw_body: str = raw_body
        self.webcase_ptrs: Optional[List[str]] = webcase_ptrs