class WebSpec:
    def __init__(self, 
                 url: str, 
                 body: str, 
                 raw_body: str,
                 screenshot: str) -> None:
        self.url: str = url
        self.body: str = body
        self.raw_body: str = raw_body
        self.screenshot: str = screenshot