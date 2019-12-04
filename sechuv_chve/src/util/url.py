import re

def extract(data: str) -> List[str]:
    return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", data)
