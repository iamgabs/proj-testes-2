# imports
import os
import sys
from src.services.exec_operations import execute_operations
from src.services.read_xml import read_xml
from typing import List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# caminho relativo para o arquivo XML
base_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_directory, 'procedimentos.xml')

if __name__ == "__main__":
    operations:List[Tuple[str, List[str]]] = read_xml(file_path)
    print(operations)
    # execute_operations(operations)