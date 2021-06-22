from unittest.mock import patch

import unittest

import app


class TestAppMethods(unittest.TestCase):
    EXPECTED_RESULT = 'Call with a valid number in the URL. ' \
                      'Example: http://127.0.0.1:5000/specialmath/7'

    def test_invalid_path_root(self):
        actual_result = app.invalid_path_root()
        self.assertEqual(self.EXPECTED_RESULT, actual_result)

    def test_invalid_path_with_a_string(self):
        some_path = '/abc'
        actual_result = app.invalid_path(some_path)
        self.assertEqual(self.EXPECTED_RESULT, actual_result)

    def test_invalid_path_with_a_long_path(self):
        some_path = '/abc/abfda'
        actual_result = app.invalid_path(some_path)
        self.assertEqual(self.EXPECTED_RESULT, actual_result)

    def test_invalid_path_with_almost_correct_but_with_string(self):
        some_path = '/specialmath/abc'
        actual_result = app.invalid_path(some_path)
        self.assertEqual(self.EXPECTED_RESULT, actual_result)

    def test_invalid_path_with_almost_correct_but_invalid_number(self):
        some_path = '/specialmath/-1'
        actual_result = app.invalid_path(some_path)
        self.assertEqual(self.EXPECTED_RESULT, actual_result)

    def test_valid_path_with_zero(self):
        args = 1
        # We imported special_math.special_math into the app module
        p = patch('app.special_math')
        mock_func = p.start()
        app.valid_path(args)
        mock_func.assert_called_once()
        mock_func.assert_called_with(args)
        p.stop()


if __name__ == '__main__':
    unittest.main()
