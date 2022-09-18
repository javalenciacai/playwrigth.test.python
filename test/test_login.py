import re
import pytest
from playwright.sync_api import expect, sync_playwright
import conftest
from baseTest import BaseTest

title = "ISIIGO"
titleQA = "Siigo Nube"
hideBrowser = True

QAColombia = [{"url":"https://qastaging.siigo.com/", "username":"siigo@techmf.com", "ValidateCompanyName":{"MenuNuevo":False,"CompanyName": "Siigo TechMF"},"title":titleQA, "ValidateENV":"qastaging"}]
QAMexico = [{"url":"http://qastaging.siigo.mx/", "username":"admin@shura.com", "ValidateCompanyName":{"MenuNuevo":True,"CompanyName": "Shura"},"title":titleQA, "ValidateENV":"qastaging"}]
QAChile = [{"url":"http://qastaging.siigo.cl/", "username":"admin@eventos.com", "ValidateCompanyName":{"MenuNuevo":True,"CompanyName": "EVENTOS EN LA NUBE"},"title":titleQA, "ValidateENV":"qastaging"}]
QAEcuador = [{"url":"http://qastaging.siigo.ec/", "username":"admin@uno.com", "ValidateCompanyName":{"MenuNuevo":True,"CompanyName": "ALMACEN TODO EN UNO"},"title":title, "ValidateENV":"qastaging"}]
Canary = [{"url":"https://siigonube.siigo.com/", "username":"calidad_nube@piloto.com", "ValidateCompanyName":{"MenuNuevo":False,"CompanyName": "PILOTO  CALIDAD  NUBE 02082022 QC"},"title":title, "ValidateENV":"siigonube2"}]


@pytest.mark.parametrize("Array",[(QAColombia), (QAMexico), (QAChile), (QAEcuador)])
def test_Login(Array):
    print(Array)    
    i = 0
    conftest.name = Array[i]["username"]
    with sync_playwright() as p:
        # Make sure to run headed.
        browser = p.chromium.launch(channel="chrome", headless=hideBrowser, slow_mo=0, timeout=60000)
        page = BaseTest(browser)
        conftest.page = page
        page.navigate(Array[i]["url"])
    

        # Expect a title "to contain" a substring.
        page.expectOfPage(re.compile(Array[i]["title"]))
        # create a locator
        txtUserName = page.locator("input[name=\"ctl14\\$txtUserName\"]")
        txtPassword = page.locator("input[name=\"ctl14\\$txtPassword\"]")
        Ingresar = page.locator("input:has-text(\"Ingresar\")")

        # Input username
        txtUserName.fill(Array[i]["username"])

        # Input password
        txtPassword.fill("1111")

        # Expect an attribute "to be strictly equal" to the value.
        expect(Ingresar).to_have_attribute("value", "Ingresar")

        # Click the get started link.
        Ingresar.click()

        # Expects the URL to contain intro.
        page.expectOfUrl(re.compile(".*" + Array[i]["ValidateENV"] + ""))

        # Validate #HeaderCompanyName
        
        if (Array[i]["ValidateCompanyName"]["MenuNuevo"]): 
            CompanyName = page.locator('fragment >> text='+Array[i]["ValidateCompanyName"]["CompanyName"]+'')   
            expect(CompanyName).to_be_visible(timeout=60000)   
        else: 
            CompanyName = page.locator("#HeaderCompanyName") 
            # Expect an attribute "to be strictly equal" to the value.
            expect(CompanyName).to_have_attribute("title", Array[i]["ValidateCompanyName"]["CompanyName"]  , timeout=20000)               

        conftest.htmlImg = page.screenshot(Array[i]["username"])
        page.contextClose()
        conftest.htmlVideo = page.video()