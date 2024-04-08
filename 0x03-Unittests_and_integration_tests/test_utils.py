#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()