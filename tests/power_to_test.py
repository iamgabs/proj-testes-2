# imports
import unittest
from src.services.exec_operations import execute_operations

class TestCasePowerTo(unittest.TestCase):

    def setUp(self):
        self.powerto_operations = [
            (
                'potenciação',
                ['2 3', '-4 2', '9 0', '5 (-2)', '2.5 3'],
                [8.0, 16.0, 1.0, 0.04, 15.625]
            )
        ]
    
    def test_power_operations(self) -> None:
        """
        Test for each sum operation in the cases.
        """
        execute_operations(self.powerto_operations)