from tree import *
from calcFatores import *
from balancear import *
from utilidade import *

def insere(raiz, valor):
    aux = raiz
    novo = Tree(valor)

    if raiz is None:
        raiz = novo
        return raiz

    while True:
        if valor < aux.val:
            if aux.esq is None:
                aux.esq = novo
                novo.pai = aux
                break
            aux = aux.esq
        else:
            if aux.dir is None:
                aux.dir = novo
                novo.pai = aux
                break
            aux = aux.dir
    raiz = calcFatores(raiz, aux)
    raiz = balancear(raiz, aux)
    return calcFatores(raiz, aux)
