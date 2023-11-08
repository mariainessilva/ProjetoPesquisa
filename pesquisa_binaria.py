def pesquisa_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro<=ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == item:
             return True
        else:
            if item < lista[meio]:
                ultimo = meio-1
            else:
                primeiro = meio+1
    return False