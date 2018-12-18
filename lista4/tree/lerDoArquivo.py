from insere import *

def lerDoArquivo():
    valores = None
    tree = None
    # terminar, dar free na arvore
    arq = open("arq1.txt", "r+")
    valores = arq.read()
    if valores is None:
        return None
    valores = valores.split(" ")
    for i in valores:
        tree = insere(tree, int(i))
    arq.close()
    return tree
