
# models/search.py
class Navigator:
    """Start navigation to url"""
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.goto(url)
