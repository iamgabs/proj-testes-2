import unittest
from src.services.exec_operations import execute_operations

class TestCaseSum(unittest.TestCase):
    
    def setUp(self):
        self.sum_operations = [
            ('soma', ['10 20', '-5 (-15)', '-1 3', '-18 0', '2.5 4.3'], [30.0, -20.0, 2.0, -18.0, 6.8])
        ]
    
    def test_sum_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        execute_operations(self.sum_operations)
