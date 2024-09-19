import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from typing import List, Tuple
from src.utils.get_operations import get_operation

def execute_operations(operations: List[Tuple[str, List[str], List[float]]]):
    """
    Executa as operações na calculadora usando o Selenium.
    
    Args:
        operations (List[Tuple[str, List[str]]]): Lista de tuplas 
        contendo a descrição da operação e uma lista de expressões.
    """
    edge_options = Options()
    edge_options.add_argument('--headless')  
    driver = webdriver.Edge(options=edge_options)

    driver.get('https://www.calculadoraonline.com.br/basica')

    for procedimento_desc, expressions, results in operations:
        print(f'\n** TESTANDO OPERAÇÃO: {procedimento_desc} **')

        for exp, res in zip(expressions, results):
            operation = get_operation(procedimento_desc, exp, res)
            print(f'{operation}')

            calc = operation.split(' =')
            calculation = calc[0].strip()

            input_field = driver.find_element(By.XPATH, '//*[@id="TIExp"]')
            input_field.clear()
            input_field.send_keys(calculation)

            driver.find_element(By.XPATH, '//*[@id="b27"]').click()

            time.sleep(1.5)

            real_result = input_field.get_attribute("value")
            print(f'--> RESULTADO OBTIDO: {real_result}\n')

    driver.quit()