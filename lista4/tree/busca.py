def busca(raiz, valor):
    aux = raiz
    while True:
        if aux is None:
            return None

        if valor < aux.val:
            aux = aux.esq
        elif valor > aux.val:
            aux = aux.dir
        else:
            return aux
