def get_operation(procedimento_desc, expression, result):
    parts = expression.split()
    
    hash_map = {
        "soma": f"{' + '.join(parts)} = {result}",
        "subtração": f"{' - '.join(parts)} = {result}",
        "multiplicação": f"{' * '.join(parts)} = {result}",
        "divisão": f"{' / '.join(parts)} = {result}",
        "potenciação": f"{parts[0]}^{parts[1]} = {result}" if len(parts) >= 2 else None
    }
    
    operation = hash_map.get(procedimento_desc)
    
    if operation is None:
        print(f"Erro: operação '{procedimento_desc}' não reconhecida ou expressão inválida.")
    
    return operation