def emOrdem(raiz):
    aux = raiz
    if aux != None:
        emOrdem(aux.esq)
        print(aux.val)
        emOrdem(aux.dir)
