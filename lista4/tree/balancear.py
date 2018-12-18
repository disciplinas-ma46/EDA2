import os
import sys
from altura import *
from calcFatores import *
from utilidade import *
from mostraArvore import *

def rotDir(raiz, no):
    temp = no.esq
    no.esq = temp.dir
    if (temp.dir != None):
        temp.dir.pai = no

    if (no.pai != None):
        if no.val < no.pai.val:
            no.pai.esq = temp
        else:
            no.pai.dir = temp

    temp.pai = no.pai
    no.pai = temp
    temp.dir = no
    no.fator = diff(no)
    raiz = calcFatores(raiz, temp)
    return raiz

def rotEsq(raiz, no):
    temp = no.dir
    no.dir = temp.esq
    if (temp.esq != None):
        temp.esq.pai = no

    if (no.pai != None):
        if no.val < no.pai.val:
            no.pai.esq = temp
        else:
            no.pai.dir = temp

    temp.pai = no.pai
    no.pai = temp
    temp.esq = no
    no.fator = diff(no)
    raiz = calcFatores(raiz, temp)
    return raiz

def balancear(raiz, no):
    aux = no
    if aux is None:
        return raiz

    while True:
        if(aux.fator > 1):
            if(aux.esq.fator < 0):
                raiz = rotEsq(raiz, aux.esq)
            raiz = rotDir(raiz, aux)
        elif(aux.fator < -1):
            if(aux.dir.fator > 0):
                raiz = rotDir(raiz, aux.dir)
            raiz = rotEsq(raiz, aux)
        aux = aux.pai
        if aux is None:
            return raiz
