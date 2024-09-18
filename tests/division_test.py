# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCaseDivision(unittest.TestCase):
    
    def setUp(self):
        self.division_operations = [
            (
                'divisão',
                ['20 4', '-15 3', '0 7', '9 2.5', '12 (-4)'],
                [5.0, -5.0, 0.0, 3.6, -3.0]
            )
        ]
    
    def test_division_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        execute_operations(self.division_operations)