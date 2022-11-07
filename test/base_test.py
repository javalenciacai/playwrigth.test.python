from playwright.sync_api import expect
import conftest
from datetime import datetime


class BaseTest:
    """The base the all tests"""
    
        
    def setUp(self) -> None:
        self.get_video()
        
    def get_video(self):
        '''get path of video and get htmlVideo'''
        path = self.video.path()
        path = path.replace("test/report/videos", "videos")
        conftest.htmlVideo = '<div><video src="%s" poster="presentation.jpg" controls></video></div>' % path

    def get_navigate(self, url, title):
        '''Start browser and validate title'''
        self.goto(url)
        expect(self).to_have_title(title)

    def get_locator(self, locator):
        '''create a locator'''
        return self.locator(locator)

    def expect_of_url(self, url_expect):
        '''Validate url expect'''
        expect(self).to_have_url(url_expect)

    def expect_element_attribute(self, element, attribute, value):
        '''Expect an attribute "to be strictly equal" to the value'''
        '''receive an element'''
        expect(element).to_have_attribute(attribute, value, timeout=20000)

    def expect_if_be_visible_continue_with_error(self, locator, message):
        '''Expect an Element if Visible but Continue With Error'''
        try:
            element_visible = BaseTest.get_locator(self, locator)
            expect(element_visible).to_be_visible(timeout=1000)
        except Exception:
            print("Elemento " + locator + " NO es visible")
        else:
            print(message)

    def expect_if_be_visible(self, locator):
        '''Expect an Element if Visible'''
        expect(locator).to_be_visible(timeout=60000)
    
    def get_screenshot(self):
        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
        name = dt_string
        img = "screenshot" + name + ".png"
        self.screenshot(path="test/report/" + img)
        html_img = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % img
        conftest.htmlImg = html_img

    def tearDown(self) -> None:
        print("hola test")