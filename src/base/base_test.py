from playwright.sync_api import expect
import conftest
from datetime import datetime


class BaseTest:
    """The base the all test_suites"""
    
        
    def setUp(self) -> None:
        self.get_video()
        
    def get_video(self):
        '''get path of video and get htmlVideo'''
        path = self.video.path()
        path = path.replace("src/report/videos", "videos")
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
        '''takes a screenshot and passes it as html code'''
        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
        name = dt_string
        img = "screenshot" + name + ".png"
        self.screenshot(path="src/report/" + img)
        html_img = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % img
        conftest.htmlImg = html_img

    def requests_api_get(self, api_request_context, url):
        '''returns a get method for an url'''
        return api_request_context.get(url)


    def requests_api_post(self, api_request_context, url, body, headers):
        '''returns a get method for an url'''
        return api_request_context.post(url, data=body, headers=headers)

    def tearDown(self) -> None:
        pass