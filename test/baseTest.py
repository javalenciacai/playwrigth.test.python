class BaseTest:
    """The base the all tests"""
    def context(browser):
        context = browser.new_context()
        page = context.new_page() 
        page.set_default_timeout(timeout=60000)
        return page
        
           

