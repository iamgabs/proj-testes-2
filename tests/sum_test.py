import unittest
from src.services.exec_operations import execute_operations

class TestCaseSum(unittest.TestCase):
    
    def setUp(self):
        self.sum_operations = [
            (
                'soma', 
                ['10 20', '-5 (-15)', '-1 3', '-18 0', '2.5 4.3'], 
                ['30', '-20', '2', '-18', '6,8']
            )
        ]
    
    def test_sum_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        obtained_results = execute_operations(self.sum_operations)

        print(f'Resultados obtidos: {obtained_results}')
        
        expected_results = self.sum_operations[0][2]

        for obtained, expected in zip(obtained_results, expected_results):
            self.assertEqual(obtained, expected)
