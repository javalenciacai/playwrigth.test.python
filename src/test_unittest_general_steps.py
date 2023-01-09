import unittest
import inspect
import pytest
from steps.general_steps import GeneralSteps



@pytest.mark.skipif(True, reason='Test is unittest')
class TestUnittestGeneralSteps(unittest.TestCase):
    
    test = GeneralSteps()   

    def test_instantiation_general_steps(self):
        """Verifica que test sea una instancia de la clase GeneralSteps"""         
        self.assertTrue(isinstance(self.test, GeneralSteps))


    def test_method_existe_in_base_test(self):
        """Verifica que exista el método en la clase GeneralSteps"""
        self.assertTrue(hasattr(GeneralSteps, 'start_navigate'))
        self.assertTrue(hasattr(GeneralSteps, 'screenshot'))


    def test_method_start_navigate_contains_arg_in_general_steps(self):
        """Verifica que start_navigate tenga los argumentos indicados en la clase GeneralSteps"""
        args = inspect.getfullargspec(self.test.start_navigate).args
        self.assertIn('self', args)
        self.assertIn('url', args)
        self.assertIn('page_title', args)


    def test_method_screenshot_contains_arg_in_general_steps(self):
        """Verifica que screenshot tenga los argumentos indicados en la clase GeneralSteps"""
        args = inspect.getfullargspec(self.test.screenshot).args
        self.assertIn('self', args)