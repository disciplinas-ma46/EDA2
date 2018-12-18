PRETO = 'p'
VERMELHO = 'v'
BRANCO = 'b'
TIPO_AVL = 'a'
TIPO_VP = 'v'

import os
import sys
sys.path.append('./tree')
from _todos import *

os.system('clear')
opcao = 1
raiz = None
#raiz = lerDoArquivo()
while opcao != 0:
    os.system('clear')
    mostraArvore(raiz, TIPO_AVL)
    opcao = menu()

    if opcao == 1:
        valor = lerValor()
        raiz = insere(raiz, valor)
    elif opcao == 2:
        valor = lerValor()
        raiz = removeValor(raiz, valor)
    elif opcao == 3:
        raiz = lerDoArquivo()
    elif opcao == 0:
        # free na arvore
        print("Saindo...")
    else:
        print("valor invalido")
        pausar()


#
