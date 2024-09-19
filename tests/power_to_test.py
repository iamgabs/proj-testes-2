# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCasePowerTo(unittest.TestCase):

    def setUp(self):
        self.powerto_operations = [
            (
                'potenciação',
                ['2 3', '-4 2', '9 0', '5 (-2)', '2.5 3'],
                ['8', '-16', '1', '0,04', '15,625']
            )
        ]
    
    def test_power_to_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        obtained_results = execute_operations(self.powerto_operations)

        print(f'Resultados obtidos: {obtained_results}')
            
        expected_results = self.powerto_operations[0][2]

        for obtained, expected in zip(obtained_results, expected_results):
            self.assertEqual(obtained, expected)