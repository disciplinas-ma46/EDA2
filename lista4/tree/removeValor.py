from busca import *
from utilidade import *
from calcFatores import *

def removeValor(raiz, valor):
    aux = None
    folha = None

    if (raiz is None):
        print("arvore esta vazia!")
        pausar()
        return raiz

    # primeiro procuramos o valor
    aux = busca(raiz, valor)
    if aux is None:
        print("valor %d nao foi encontrado!" % valor)
        pausar()
        return raiz

    # caso nao houver filhos
    if ((aux.esq == None) and (aux.dir == None)):
        # é nó raiz
        if aux.pai == None:
            return None
        if (aux.pai.val > valor):
            aux.pai.esq = None
        else:
            aux.pai.dir = None

        return raiz

    # caso tiver filho so a esquerda
    if ((aux.esq != None) and (aux.dir == None)):
        if (aux.pai.val > valor):
            aux.pai.esq = aux.esq
        else:
            aux.pai.dir = aux.esq
        return calcFatores(raiz, aux)

    # caso tiver filho so a direita
    if ((aux.esq == None) and (aux.dir != None)):
        if (aux.pai.val > valor):
            aux.pai.esq = aux.dir
        else:
            aux.pai.dir = aux.dir
        return calcFatores(raiz, aux)

    #caso o No tiver 2 filhos
    folha = aux.dir
    if folha.esq is None:
        aux.dir = folha.dir
        if folha.dir != None:
            folha.dir.pai = aux
    else:
        while (folha.esq != None):
            folha = folha.esq
        folha.pai.esq = folha.dir
    aux.val = folha.val

    return calcFatores(raiz, folha)
