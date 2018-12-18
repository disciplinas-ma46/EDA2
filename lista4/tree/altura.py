def altura(raiz):
    aux = raiz
    if aux is None:
        return 0
    altEsq = altura(aux.esq)
    altDir = altura(aux.dir)
    if altEsq > altDir:
        return altEsq+1
    else:
        return altDir+1

def diff(no):
    if no is None:
        return 0
    e = altura(no.esq)
    d = altura(no.dir)
    return e - d
