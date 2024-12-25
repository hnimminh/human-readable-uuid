import unittest
from unittest import mock

import hrid


class TestGenerateFunction(unittest.TestCase):

    def setUp(self):
        self.hrid = hrid.HRID()
        self.hrid.delimiter = ', '
        self.hrid.random = mock.Mock()
        self.hrid.random.choice.side_effect = lambda x: x[0]

    def test_transform_string_element(self):
        element = 'adjective'
        expected_output = hrid.word_lists.WORD_LISTS['adjective']
        self.assertEqual(self.hrid._transform_element(element), expected_output)

    def test_transform_list_element(self):
        element = ['hello', 'hi']
        self.assertEqual(self.hrid._transform_element(element), element)

    def test_transform_unknown_element(self):
        element = 'unknown'
        expected_output = [element]
        self.assertEqual(self.hrid._transform_element(element), expected_output)

    def test_string_elements_only(self):
        self.hrid._elements = [['hello'], ['world']]
        expected_output = 'hello, world'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_list_elements_only(self):
        self.hrid._elements = [['hello', 'hi'], ['world', 'earth']]
        expected_output = 'hello, world'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_mixed_string_and_list_elements(self):
        self.hrid._elements = [['hello'], ['world', 'earth'], ['again']]
        expected_output = 'hello, world, again'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_empty_elements(self):
        self.hrid._elements = []
        expected_output = ''
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_none_elements(self):
        self.hrid._elements = None
        with self.assertRaises(TypeError):
            self.hrid.generate()


if __name__ == '__main__':
    unittest.main()
