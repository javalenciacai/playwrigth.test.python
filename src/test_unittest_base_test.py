import unittest
import inspect
import pytest
from base.base_test import BaseTest


@pytest.mark.skipif(True, reason='Test is unittest')
class TestUnittestBaseTest(unittest.TestCase):
    
    test = BaseTest()
    
    def test_instantiation_base_test(self):
        """Verifica que test sea una instancia de la clase BaseTest"""
        
        self.assertTrue(isinstance(self.test, BaseTest))

    def test_method_existe_in_base_test(self):
        """Verifica que exista el método en la clase BaseTest"""
        self.assertTrue(hasattr(BaseTest, 'get_video'))
        self.assertTrue(hasattr(BaseTest, 'get_navigate'))
        self.assertTrue(hasattr(BaseTest, 'get_locator'))
        self.assertTrue(hasattr(BaseTest, 'expect_of_url'))
        self.assertTrue(hasattr(BaseTest, 'expect_element_attribute'))
        self.assertTrue(hasattr(BaseTest, 'expect_if_be_visible_continue_with_error'))
        self.assertTrue(hasattr(BaseTest, 'expect_if_be_visible'))
        self.assertTrue(hasattr(BaseTest, 'get_screenshot'))
        self.assertTrue(hasattr(BaseTest, 'requests_api_get'))
        self.assertTrue(hasattr(BaseTest, 'requests_api_post'))
        self.assertTrue(hasattr(BaseTest, 'setUp'))

    def test_method_get_video_contains_arg_in_base_test(self):
        """Verifica que get_video tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.get_video).args
        self.assertIn('self', args)


    def test_method_get_navigate_contains_arg_in_base_test(self):
        """Verifica que get_navigate tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.get_navigate).args
        self.assertIn('self', args)
        self.assertIn('url', args)
        self.assertIn('title', args)


    def test_method_get_locator_contains_arg_in_base_test(self):
        """Verifica que get_locator tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.get_locator).args
        self.assertIn('self', args)
        self.assertIn('locator', args)

    def test_method_expect_of_url_contains_arg_in_base_test(self):
        """Verifica que expect_of_url tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.expect_of_url).args
        self.assertIn('self', args)
        self.assertIn('url_expect', args)

    def test_method_expect_element_attribute_contains_arg_in_base_test(self):
        """Verifica que expect_element_attribute tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.expect_element_attribute).args
        self.assertIn('self', args)
        self.assertIn('element', args)
        self.assertIn('attribute', args)
        self.assertIn('value', args)

    def test_method_expect_if_be_visible_continue_with_error_contains_arg_in_base_test(self):
        """Verifica que expect_if_be_visible_continue_with_error tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.expect_if_be_visible_continue_with_error).args
        self.assertIn('self', args)
        self.assertIn('locator', args)
        self.assertIn('message', args)

    def test_method_expect_if_be_visible_contains_arg_in_base_test(self):
        """Verifica que expect_if_be_visible tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.expect_if_be_visible).args
        self.assertIn('self', args)
        self.assertIn('locator', args)

    def test_method_get_screenshot_contains_arg_in_base_test(self):
        """Verifica que get_screenshot tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.get_screenshot).args
        self.assertIn('self', args)

    def test_method_requests_api_get_contains_arg_in_base_test(self):
        """Verifica que requests_api_get tenga los argumentos indicados en la clase BaseTest"""
        args = inspect.getfullargspec(self.test.requests_api_get).args
        self.assertIn('self', args)
        self.assertIn('api_request_context', args)
        self.assertIn('url', args)

    