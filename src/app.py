# imports
from services.exec_operations import execute_operations
from services.read_xml import read_xml
from typing import List, Tuple

file_path = 'C:/Users/conta/proj-testes-2/src/procedimentos.xml'

if __name__ == "__main__":
    operations:List[Tuple[str, List[str]]] = read_xml()
    execute_operations()