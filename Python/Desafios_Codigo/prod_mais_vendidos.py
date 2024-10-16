def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        if max_produto == None:
            max_produto = produto
            max_count = count 
        else:
            if count > max_count:
                max_produto = produto
                max_count = count
            else:
                continue    
                
        
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    entrada = entrada.split(",")
    produtos = [x.strip() for x in entrada]
    
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))