from base.base_test import BaseTest
from repository.repository_login import RepositoryLogin
from repository.repository_login_from_manager import RepositoryLoginFromManager
from playwright.sync_api import expect
import re


class LoginSteps:

    def login(self, username, password):
        '''you are login on app'''

        # create a locator
        txt_user_name = BaseTest.get_locator(self, RepositoryLogin.txt_user_name)
        txt_password = BaseTest.get_locator(self, RepositoryLogin.txt_password)
        btn_login = BaseTest.get_locator(self, RepositoryLogin.btn_login)

        # Expect an attribute "to be strictly equal" to the value.
        BaseTest.expect_element_attribute(self, btn_login, "value", "Ingresar")

        # Input username
        txt_user_name.fill(username)

        # Input password
        txt_password.fill(password)        

        # Click the get started link.
        btn_login.click()


    def login_from_manager(self, username, password):
        '''you are login on app'''
        # create a locator
        txt_user_name = BaseTest.get_locator(self, RepositoryLoginFromManager.txt_user_name)
        txt_password = BaseTest.get_locator(self, RepositoryLoginFromManager.txt_password)
        btn_login = BaseTest.get_locator(self, RepositoryLoginFromManager.btn_login)

        # Input username
        txt_user_name.fill(username)

        # Input password
        txt_password.fill(password)

        # Expect an attribute "to be strictly equal" to the value.
        BaseTest.expect_element_attribute(self, btn_login, "text", "Ingresar")

        # Click the get started link.
        btn_login.click()

    def validate_company_on_update(self):
        '''Validate if the page is on update'''
        BaseTest.expect_if_be_visible_continue_with_error(self, RepositoryLogin.reload_page, "Empresa en actualización")

    def validate_correct_environment(self, environment):
        '''Expect the URL to contains intro'''
        BaseTest.expect_of_url(self, re.compile(".*" + environment + ""))

    def validate_company_name(self, new_menu, company_name):
        '''Validate #HeaderCompanyName'''
        
        if (new_menu):
            locator_company_name_new_menu = BaseTest.get_locator(self, 'fragment >> text=' + company_name + '')
            BaseTest.expect_if_be_visible(self, locator_company_name_new_menu)
        else:
            locator_company_name = BaseTest.get_locator(self, RepositoryLogin.header_company_name)
            BaseTest.expect_element_attribute(self, locator_company_name, "title", company_name)
