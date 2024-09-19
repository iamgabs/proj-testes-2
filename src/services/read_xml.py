import xml.etree.ElementTree as ET
from typing import List, Tuple

def read_xml(file_path: str) -> List[Tuple[str, List[str], List[float]]]:
    """
    Lê o arquivo XML e retorna uma lista de operações a serem executadas com o resultado esperado.
    
    Args:
        file_path (str): Caminho para o arquivo XML.
    
    Returns:
        List[Tuple[str, List[str]]]: Lista de tuplas contendo a descrição da operação, 
        uma lista de expressões e o resultado esperado.
    """
    operations = []

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

    except ET.ParseError as e:
        print(f"Erro ao ler o arquivo XML: {e}")
        return operations

    for procedimento in root.findall('procedimento'):
        procedimento_desc = procedimento.get('desc').lower()

        if procedimento_desc not in ["soma", "subtração", "multiplicação", "divisão", "potenciação"]:
            print(f'Operação "{procedimento_desc}" não suportada.')
            continue

        expressions = []
        results = []

        for caso in procedimento.findall('caso'):

            dados = [dado.text for dado in caso if dado.tag != 'resultado']
            expression = " ".join(dados)
            result = float(caso.find('resultado').text)

            expressions.append(expression)
            results.append(result)

            

        operations.append((procedimento_desc, expressions, results))

    return operations