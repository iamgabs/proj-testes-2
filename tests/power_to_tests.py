# imports
import unittest
from src.services.power_to import DoPower_To as operation

class TestCasePowerTo(unittest.TestCase):

    def test_power_to_empty_list(self) -> None:
        self.assertEqual(operation.do_power_to([]), 0)

    def test_power_to_single_element(self) -> None:
        self.assertEqual(operation.do_power_to([5]), 5)
    
    def test_power_to_two_elements(self) -> None:
        self.assertEqual(operation.do_power_to([5, 5]), 3125)

    def test_power_to_multiple_elements(self) -> None:
        self.assertEqual(operation.do_power_to([1, 2, 3]), 0)

    def test_power_to_negative_numbers(self) -> None:
        self.assertEqual(operation.do_power_to([-1, -2]), 1)

    def test_power_to_mixed_numbers(self) -> None:
        self.assertAlmostEqual(operation.do_power_to([5, -2]), 0.04)