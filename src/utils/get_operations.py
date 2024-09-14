def get_operation(procedimento_desc, expression):
    parts = expression.split()
    
    hash_map = {
        "soma": " + ".join(parts),
        "subtração": " - ".join(parts),
        "multiplicação": " * ".join(parts),
        "divisão": " / ".join(parts),
        "potenciação": f"{parts[0]}^{parts[1]}" if len(parts) >= 2 else None
    }
    
    operation = hash_map.get(procedimento_desc)
    
    if operation is None:
        print(f"Erro: operação '{procedimento_desc}' não reconhecida ou expressão inválida.")
    
    return operation