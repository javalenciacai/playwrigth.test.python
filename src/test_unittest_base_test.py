import unittest

import pytest
from base.base_test import BaseTest
from steps.general_steps import GeneralSteps
from steps.login_steps import LoginSteps


@pytest.mark.skipif(True, reason='Test is unittest')
class TestBaseTest(unittest.TestCase):
    
    
    def test_instantiation_base_test(self):
        # Crea una instancia de la clase BaseTest
        test = BaseTest()
        
        # Verifica que test sea una instancia de la clase BaseTest
        self.assertTrue(isinstance(test, BaseTest))

    def test_instantiation_general_steps(self):
        # Crea una instancia de la clase BaseTest
        test = GeneralSteps()
        
        # Verifica que test sea una instancia de la clase BaseTest
        self.assertTrue(isinstance(test, GeneralSteps))


    def test_instantiation_login_steps(self):
        # Crea una instancia de la clase BaseTest
        test = LoginSteps()
        
        # Verifica que test sea una instancia de la clase BaseTest
        self.assertTrue(isinstance(test, LoginSteps))