#!/usr/bin/env python3
import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize
class TestAccessNestedMap(unittest.TestCase):

    def test_access_nested_map(self):
        test_cases = [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
        for nested_map, path, expected in test_cases:
            self.assertEqual(access_nested_map(nested_map, path), expected)




class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):
    def test_get_json(self):
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            with patch("utils.requests.get") as mock_get:
                mock_response = Mock()
                mock_response.json.return_value = test_payload
                mock_get.return_value = mock_response

                result = get_json(test_url)

                # Check the output
                self.assertEqual(result, test_payload)

               
                mock_get.assert_called_once_with(test_url)

from utils import memoize
def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create instance of TestClass
        test_obj = TestClass()

        # Patch a_method to monitor calls
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()
