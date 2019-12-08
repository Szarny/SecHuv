from typing import Optional, List
from mypy_extensions import TypedDict

class MailSpec(TypedDict):
    from_addr: str
    spf_status: str
    dkim_status: str
    is_html: bool
    subject: str
    body: Optional[str]
    raw_body: str