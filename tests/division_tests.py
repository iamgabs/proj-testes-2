# imports
import unittest
from src.services.division import Dodivision as operation

class TestCaseDivision(unittest.TestCase):
    
    def test_division_empty_list(self) -> None:
        self.assertEqual(operation.do_division([]), 0)

    def test_division_single_element(self) -> None:
        self.assertEqual(operation.do_division([5]), 5)

    def test_division_two_elements(self) -> None:
        self.assertEqual(operation.do_division([4, 2]), 2)

    def test_division_multiple_elements(self) -> None:
        self.assertAlmostEqual(operation.do_division([1, 2, 3]), 0.16666666666)

    def test_division_negative_numbers(self) -> None:
        self.assertAlmostEqual(operation.do_division([-1, -2, -3]), -0.16666666666)

    def test_division_mixed_numbers(self) -> None:
        self.assertAlmostEqual(operation.do_division([1, -1, 2, -2, 3, -3]), -0.02777777777)