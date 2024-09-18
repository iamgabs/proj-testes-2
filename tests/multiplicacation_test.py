# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCaseMultiplication(unittest.TestCase):
    
    def setUp(self):
        self.multiplication_operations = [
            (
                'multiplicação',
                ['5 3', '-4 7', '0 12', '6.5 2.0', '-3 (-8)'],
                [15.0, -28.0, 0.0, 13.0, 24.0]
            )
        ]
    
    def test_multiplication_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        execute_operations(self.multiplication_operations)