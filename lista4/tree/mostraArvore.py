from altura import *
from cores import *
from defines import *
from utilidade import *

def estilo(no):
    valor = no.val
    if valor < 0:
        valor *= (-1)
    if no.pai is None:
        return "white"
    if (valor > no.pai.val):
        return "YELLOW"
    return "white"

def printaValor(no, tipo):
    if (tipo == TIPO_VP):
        if (no.cor == VERMELHO):
            printColorido(str(no.val),"normal","red")
        else:
            printColorido(str(no.val),"normal","black")
    else:
        #printColorido(str(no.val),list(Cor.fore.keys())[no.val%10],"white")
        printColorido(str(no.val),"black",estilo(no))

def printaRecursivo(node, tipo, sizeLine, posX, posY):
    no = node
    gotoxy(posX, posY)
    printaValor(no,tipo)
    if (no.esq != None):
        i = 1
        while (i <= sizeLine):
            gotoxy(posX-i, posY+i)
            print("/",end="")
            i += 1
        printaRecursivo(no.esq, tipo, sizeLine//2, posX-sizeLine, posY+sizeLine+1)

    if (no.dir != None):
        i = 1
        while (i <= sizeLine):
            gotoxy(posX+i, posY+i)
            print("\\",end="")
            i += 1
        printaRecursivo(no.dir, tipo, sizeLine//2, posX+sizeLine, posY+sizeLine+1)

def strTipo(tipo):
    if tipo == TIPO_VP:
        return "vermelho/preto"
    return "AVL (cor para diferenciar n°s encostados)"

def mostraArvore(arvore, tipo):
    h = altura(arvore)-1
    sizeTree = 1
    posX = sizeTree*(2**h)
    posY = 5
    tamLinha = 49
    
    print(" ","="*tamLinha)
    print(" | Arvore %-30s|" % strTipo(tipo))
    print(" ","="*tamLinha)
    if (arvore != None):
        printaRecursivo(arvore, tipo, sizeTree*(posX//2), sizeTree*posX, posY)
        gotoxy(1,sizeTree*posX+h+9)
    else:
        print("Sem arvore carregada")
