from typing import Optional, List
from mypy_extensions import TypedDict

class MailSpec(TypedDict):
    from_addr: str
    spf_status: str
    dkim_status: str
    subject: str
    body: str
    attach_files: List[str]