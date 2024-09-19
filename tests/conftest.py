# imports 
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest
from .sum_test import TestCaseSum
from .sub_test import TestCaseSubtraction
from .division_test import TestCaseDivision
from .multiplicacation_test import TestCaseMultiplication
from .power_to_test import TestCasePowerTo
from .read_xml_test import TestCaseReadXml

if __name__ == "__main__":
    unittest.main()