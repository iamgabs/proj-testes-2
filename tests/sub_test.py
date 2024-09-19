import unittest
from src.services.exec_operations import execute_operations

class TestCaseSubtraction(unittest.TestCase):
    def setUp(self):
        self.subtraction_operations = [
            (
                'subtração', 
                ['25 10', '-8 3', '0 (-12)', '50 100', '12.75 4.25'], 
                ['15', '-11', '12', '-50', '8,5']
            )
        ]
    
    def test_subtraction_operations(self) -> None:
        """
        Test for each subtraction operation in the cases.
        """
        obtained_results = execute_operations(self.subtraction_operations)

        print(f'Resultados obtidos: {obtained_results}')
        
        expected_results = self.subtraction_operations[0][2]

        for obtained, expected in zip(obtained_results, expected_results):
            self.assertEqual(obtained, expected)