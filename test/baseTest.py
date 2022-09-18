import re
from playwright.sync_api import expect

class BaseTest:
    """The base the all tests"""
    def __init__(self, browser):
        self.context = browser.new_context(record_video_dir="test/report/videos/")
        page = self.context.new_page() 
        page.set_default_timeout(timeout=60000)
        self.page = page
        

    def navigate(self, url):
        return self.page.goto(url)


    def locator(self, locator):
        return self.page.locator(locator)


    def screenshot(self, name):
        img = "screenshot"+name+".png"        
        self.page.screenshot(path="test/report/"+img)
        htmlImg = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%img
        return htmlImg

    def expectOfUrl(self, urlExpect):
        return expect(self.page).to_have_url(urlExpect)

    def expectOfPage(self, valueExpect):
        return expect(self.page).to_have_title(valueExpect)

    def contextClose(self):
        self.context.close()

    def video(self):
        path = self.page.video.path()
        htmlVideo = '<div><video src="../../%s" poster="presentacion.jpg" controls></video></div>'%path
        return htmlVideo