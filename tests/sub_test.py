import unittest
from src.services.exec_operations import execute_operations

class TestCaseSubtraction(unittest.TestCase):
    def setUp(self):
        self.subtraction_operations = [
            (
                'subtração', 
                ['25 10', '-8 3', '0 (-12)', '50 100', '12.75 4.25'], 
                [15.0, -11.0, 12.0, -50.0, 8.5]
            )
        ]
    
    def test_subtraction_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        execute_operations(self.subtraction_operations)
