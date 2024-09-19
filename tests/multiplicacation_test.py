# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCaseMultiplication(unittest.TestCase):
    
    def setUp(self):
        self.multiplication_operations = [
            (
                'multiplicação',
                ['5 3', '-4 7', '0 12', '6.5 2.0', '-3 (-8)'],
                ['15', '-28', '0', '13', '24']
            )
        ]
    
    def test_multiplication_operations(self) -> None:
        """
        Test for each multiplication operation in the cases.
        """
        obtained_results = execute_operations(self.multiplication_operations)

        print(f'Resultados obtidos: {obtained_results}')
        
        expected_results = self.multiplication_operations[0][2]

        for obtained, expected in zip(obtained_results, expected_results):
            self.assertEqual(obtained, expected)