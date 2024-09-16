# imports
import unittest
from src.services.sub import DoSub as operation

class TestCaseSubtraction(unittest.TestCase):
    
    def test_sub_empty_list(self) -> None:
        self.assertEqual(operation.do_sub([]), 0)

    def test_sub_single_element(self) -> None:
        self.assertEqual(operation.do_sub([5]), 5)

    def test_sub_multiple_elements(self) -> None:
        self.assertEqual(operation.do_sub([1, 2, 3]), -4)

    def test_sub_negative_numbers(self) -> None:
        self.assertEqual(operation.do_sub([(-1), (-2), (-3)]), 4)

    def test_sub_mixed_numbers(self) -> None:
        self.assertEqual(operation.do_sub([1, (-1), 2, (-2), 3, (-3)]), 2)