import pytest
from playwright.sync_api import Page
import conftest
from data_test.data_login import DataLogin
from steps.login_steps import LoginSteps
from steps.general_steps import  GeneralSteps


class TestClass:

    conftest.htmlImg = ''
    conftest.htmlVideo = ''
    
    
    @pytest.mark.parametrize("testdata", [(DataLogin.qa_colombia),(DataLogin.qa_chile),(DataLogin.qa_ecuador)])
    def test_login(self, page: Page, testdata) -> None:
        i = 0
        print(testdata[i]["url"])
        print(testdata[i]["username"])
        GeneralSteps.start_navigate(page,testdata[i]["url"], testdata[i]["title"])    
        LoginSteps.login(page, testdata[i]["username"], "1111")
        LoginSteps.validate_company_on_update(page)        
        LoginSteps.validate_correct_environment(page, testdata[i]["ValidateENV"])
        LoginSteps.validate_company_name(page,testdata[i]["ValidateCompanyName"]["MenuNuevo"], testdata[i]["ValidateCompanyName"]["CompanyName"])
        GeneralSteps.screenshot(page)
        
    
    

    @pytest.mark.parametrize("testdata", [(DataLogin.qa_mexico)])
    def test_login_front_manager(self, page: Page, testdata) -> None:
        i = 0
        GeneralSteps.start_navigate(page,testdata[i]["url"], testdata[i]["title"])
        LoginSteps.login_from_manager(page, testdata[i]["username"], "1111")
        LoginSteps.validate_company_on_update(page)        
        LoginSteps.validate_correct_environment(page, testdata[i]["ValidateENV"])     
        LoginSteps.validate_company_name(page,testdata[i]["ValidateCompanyName"]["MenuNuevo"], testdata[i]["ValidateCompanyName"]["CompanyName"])        
        GeneralSteps.screenshot(page)
