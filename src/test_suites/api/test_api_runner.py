import pytest
from base.base_test import BaseTest
import conftest




class TestApiRunner:
     

    conftest.baseUrl = 'https://servicesqa.siigo.com/'


    @pytest.mark.parametrize("testdata", ["ACClosingApi/","ACCostingApi/","ACEntryApi/","ACGeneralApi/","ACMagneticApi/","AcPayrollApi/","ACRecoveryApi/","ACReportApi/","WorkFlowApi/"])
    def test_get_api_runner(self, api_request_context, testdata):
        """ test api runner"""
        response = BaseTest.requests_api_get(self, api_request_context, testdata)
        assert response.status == 200
