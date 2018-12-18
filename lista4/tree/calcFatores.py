# recebe um nó, e atualiza os fatores dos ancestrais
# retorna a raiz
from altura import *

def calcFatores(raiz, no):
    aux = no
    if aux is None:
        return None
    if aux.pai == None:
        aux.fator = diff(aux)
        return aux
    while aux.pai != None:
        aux.fator = diff(aux)
        aux = aux.pai
    aux.fator = diff(aux)
    return raiz
