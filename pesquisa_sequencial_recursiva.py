def pesquisa(lista, n):
    if lista[0] == n:
        return True
    if len(lista) == 1:
        return False
    return pesquisa(lista[1:], n)