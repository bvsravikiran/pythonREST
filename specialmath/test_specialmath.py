import unittest
from unittest.mock import patch

import specialmath


class TestSpecialMathNaive(unittest.TestCase):
    def test_special_math_naive_zero_negative_one(self):
        num = -1
        expected_result = num
        actual_result = specialmath.special_math_naive(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_naive_zero(self):
        num = 0
        expected_result = 0
        actual_result = specialmath.special_math_naive(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_naive_one(self):
        num = 1
        expected_result = 1
        actual_result = specialmath.special_math_naive(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_naive_two(self):
        num = 2
        expected_result = 3
        actual_result = specialmath.special_math_naive(num)
        self.assertEqual(expected_result, actual_result)


class TestSpecialMathTopDown(unittest.TestCase):
    HELPER_FUNCTION_NAME = 'specialmath.top_down_helper'

    def test_special_math_top_down_negative_num(self):
        num = -1
        expected_result = num
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_does_call_helper_negative_one(self):
        num = -1
        p = patch(self.HELPER_FUNCTION_NAME)
        mock_func = p.start()
        specialmath.special_math_top_down(num)
        mock_func.assert_not_called()
        p.stop()

    def test_special_math_top_down_zero(self):
        num = 0
        expected_result = 0
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_does_call_helper_zero(self):
        num = 0
        p = patch(self.HELPER_FUNCTION_NAME)
        mock_func = p.start()
        specialmath.special_math_top_down(num)
        mock_func.assert_not_called()
        p.stop()

    def test_special_math_top_down_one(self):
        num = 1
        expected_result = 1
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_does_call_helper_one(self):
        num = 1
        p = patch(self.HELPER_FUNCTION_NAME)
        mock_func = p.start()
        specialmath.special_math_top_down(num)
        mock_func.assert_not_called()
        p.stop()

    def test_special_math_top_down_two(self):
        num = 2
        expected_result = 3
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_calls_helper_two(self):
        num = 2
        dic = [0, 1, -1]
        p = patch(self.HELPER_FUNCTION_NAME)
        mock_func = p.start()
        specialmath.special_math_top_down(num)
        mock_func.assert_called_once()
        mock_func.assert_called_with(2, dic)
        p.stop()

    def test_special_math_top_down_seven(self):
        num = 7
        expected_result = 79
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_calls_helper_seven(self):
        num = 7
        dic = [0, 1, -1, -1, -1, -1, -1, -1]
        p = patch(self.HELPER_FUNCTION_NAME)
        mock_func = p.start()
        specialmath.special_math_top_down(num)
        mock_func.assert_called_once()
        mock_func.assert_called_with(7, dic)
        p.stop()

    def test_special_math_top_down_seventeen(self):
        num = 17
        expected_result = 10926
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_top_down_ninety(self):
        num = 90
        expected_result = 19740274219868223074
        actual_result = specialmath.special_math_top_down(num)
        self.assertEqual(expected_result, actual_result)


class TestTopDownHelper(unittest.TestCase):
    def test_top_down_helper_zero_negative_one(self):
        num = -1
        dic = [0, 1, -1]
        expected_result = num
        actual_result = specialmath.top_down_helper(num, dic)
        self.assertEqual(expected_result, actual_result)

    def test_top_down_helper_zero(self):
        num = 0
        dic = [0, 1, -1]
        expected_result = dic[0]
        actual_result = specialmath.top_down_helper(num, dic)
        self.assertEqual(expected_result, actual_result)

    def test_top_down_helper_one(self):
        num = 1
        dic = [0, 1, -1]
        expected_result = dic[1]
        actual_result = specialmath.top_down_helper(num, dic)
        self.assertEqual(expected_result, actual_result)

    def test_top_down_helper_two(self):
        num = 2
        dic = [0, 1, -1]
        expected_result = 3
        actual_result = specialmath.top_down_helper(num, dic)
        self.assertEqual(expected_result, actual_result)

    def test_top_down_helper_seven(self):
        num = 7
        dic = [0, 1, -1, -1, -1, -1, -1, -1]
        expected_result = 79
        actual_result = specialmath.top_down_helper(num, dic)
        self.assertEqual(expected_result, actual_result)


class TestSpecialMathBottomUp(unittest.TestCase):
    def test_special_math_bottom_up_zero(self):
        num = 0
        expected_result = 0
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_up_one(self):
        num = 1
        expected_result = 1
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_up_two(self):
        num = 2
        expected_result = 3
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_up_seven(self):
        num = 7
        expected_result = 79
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_up_seventeen(self):
        num = 17
        expected_result = 10926
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_up_ninety(self):
        num = 90
        expected_result = 19740274219868223074
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)

    def test_special_math_bottom_less_than_zero_negative_one(self):
        num = -1
        expected_result = num
        actual_result = specialmath.special_math_bottom_up(num)
        self.assertEqual(expected_result, actual_result)


class TestSpecialMath(unittest.TestCase):
    def test_special_math_does_not_calls_special_math_bottom_up_with_negative(self):
        num = -1
        p = patch('specialmath.special_math_bottom_up')
        mock_func = p.start()
        specialmath.special_math(num)
        mock_func.assert_not_called()
        p.stop()

    def test_special_math_calls_special_math_bottom_up_with_zero(self):
        num = 0
        p = patch('specialmath.special_math_bottom_up')
        mock_func = p.start()
        specialmath.special_math(num)
        mock_func.assert_called_once()
        mock_func.assert_called_with(num)
        p.stop()

    def test_special_math_calls_special_math_bottom_up_with_one(self):
        num = 1
        p = patch('specialmath.special_math_bottom_up')
        mock_func = p.start()
        specialmath.special_math(num)
        mock_func.assert_called_once()
        mock_func.assert_called_with(num)
        p.stop()


if __name__ == '__main__':
    unittest.main()
