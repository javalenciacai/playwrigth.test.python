from base_test import BaseTest

class GeneralSteps:


    def start_navigate(self, url, page_title):     
        BaseTest.get_video(self)            
        BaseTest.get_navigate(self, url, page_title)
    
    def screenshot(self):
        BaseTest.get_screenshot(self)
    