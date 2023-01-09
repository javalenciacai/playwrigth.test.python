import unittest
import inspect
import pytest

from steps.login_steps import LoginSteps



@pytest.mark.skipif(True, reason='Test is unittest')
class TestUnittestLoginSteps(unittest.TestCase):
    
    test = LoginSteps()   

    def test_instantiation_login_steps(self):
        """Verifica que test sea una instancia de la clase LoginSteps"""
        test = LoginSteps()
        self.assertTrue(isinstance(test, LoginSteps))

    def test_method_existe_in_login_steps(self):
        """Verifica que exista el método en la clase LoginSteps"""
        self.assertTrue(hasattr(LoginSteps, 'login'))
        self.assertTrue(hasattr(LoginSteps, 'validate_correct_environment'))
        self.assertTrue(hasattr(LoginSteps, 'validate_company_name'))

    def test_method_login_contains_arg_in_login_steps(self):
        """Verifica que login tenga los argumentos indicados en la clase LoginSteps"""
        args = inspect.getfullargspec(self.test.login).args
        self.assertIn('self', args)
        self.assertIn('username', args)
        self.assertIn('password', args)

    def test_method_validate_correct_environment_contains_arg_in_login_steps(self):
        """Verifica que validate_correct_environment tenga los argumentos indicados en la clase GeneralSteps"""
        args = inspect.getfullargspec(self.test.validate_correct_environment).args
        self.assertIn('self', args)
        self.assertIn('environment', args)

    def test_method_validate_company_name_contains_arg_in_login_steps(self):
        """Verifica que validate_company_name tenga los argumentos indicados en la clase GeneralSteps"""
        args = inspect.getfullargspec(self.test.validate_company_name).args
        self.assertIn('self', args)
















    


    


    