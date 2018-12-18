import sys

def pausar():
    print("\nPressione enter para continuar ")
    str = sys.stdin.readline()
    a = 1

def lerValor():
    print("Digite o valor: ")
    valor = sys.stdin.readline()
    # terminar, validar opcao para ser int
    return int(valor);


def gotoxy(x,y):
    print("\033[{};{}H".format(y, x), end="")

def moveUp(x):
    print("\033[{}A".format(x), end="")
def moveDown(x):
    print("\033[{}B".format(x), end="")
def moveRight(x):
    print("\033[{}C".format(x), end="")
def moveLeft(x):
    print("\033[{}D".format(x), end="")
'''
import os
os.system('clear')
gotoxy(10, 2)
print("oi")
'''
