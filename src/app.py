# imports
import os
from services.exec_operations import execute_operations
from services.read_xml import read_xml
from typing import List, Tuple

# caminho relativo para o arquivo XML
base_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_directory, 'procedimentos.xml')

if __name__ == "__main__":
    operations:List[Tuple[str, List[str]]] = read_xml(file_path)
    execute_operations(operations)