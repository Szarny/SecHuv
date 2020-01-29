from mypy_extensions import TypedDict

class WebSpec(TypedDict):
    url: str
    body: str
    raw_body: str
    screenshot: str
    summary: str