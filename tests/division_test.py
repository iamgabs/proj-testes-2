# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCaseDivision(unittest.TestCase):
    
    def setUp(self):
        self.division_operations = [
            (
                'divisão',
                ['20 4', '-15 3', '0 7', '9 2.5', '12 (-4)'],
                ['5', '-5', '0', '3,6', '-3']
            )
        ]
    
    def test_division_operations(self) -> None:
        """
        Test for each division operation in the cases.
        """
        obtained_results = execute_operations(self.division_operations)

        print(f'Resultados obtidos: {obtained_results}')
        
        expected_results = self.division_operations[0][2]

        for obtained, expected in zip(obtained_results, expected_results):
            self.assertEqual(obtained, expected)