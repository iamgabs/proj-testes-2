# imports
import unittest
from src.services.sum import DoSum as operation

class TestCaseSum(unittest.TestCase):

    def test_sum_empty_list(self) -> None:
        self.assertEqual(operation.do_sum([]), 0)

    def test_sum_single_element(self) -> None:
        self.assertEqual(operation.do_sum([5]), 5)

    def test_sum_multiple_elements(self) -> None:
        self.assertEqual(operation.do_sum([1, 2, 3]), 6)

    def test_sum_negative_numbers(self) -> None:
        self.assertEqual(operation.do_sum([-1, -2, -3]), -6)

    def test_sum_mixed_numbers(self) -> None:
        self.assertEqual(operation.do_sum([1, -1, 2, -2, 3, -3]), 0)