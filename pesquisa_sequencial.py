def pesquisa_sequencia(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
    return encontrado