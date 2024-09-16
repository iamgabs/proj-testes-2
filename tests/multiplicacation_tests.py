# imports
import unittest
from src.services.multiply import DoMultiply as operation
class TestCaseMultiplication(unittest.TestCase):
    
    def test_multiply_empty_list(self) -> None:
        self.assertEqual(operation.do_multiply([]), 1)

    def test_multiply_single_element(self) -> None:
        self.assertEqual(operation.do_multiply([5]), 5)

    def test_multiply_multiple_elements(self) -> None:
        self.assertEqual(operation.do_multiply([1, 2, 3]), 6)

    def test_multiply_negative_numbers(self) -> None:
        self.assertEqual(operation.do_multiply([-1, -2, -3]), -6)

    def test_multiply_mixed_numbers(self) -> None:
        self.assertEqual(operation.do_multiply([1, -1, 2, -2, 3, -3]), -36)