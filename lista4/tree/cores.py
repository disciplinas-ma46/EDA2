class Cor:
    fore = {
        "BLACK":30,
        "RED":31,
        "GREEN":32,
        "YELLOW":33,
        "BLUE":34,
        "MARGENTA":35,
        "CYAN":36,
        "WHITE":37,#37
        "BLACK1":30,#nao tem
        "BLACK2":30,#nao tem
        "NORMAL":39,
    }
    back = {
        "BLACK":40,
        "RED":41,
        "GREEN":42,
        "YELLOW":43,
        "BLUE":44,
        "MAGENTA":45,
        "CYAN":46,
        "WHITE":47,
        "NORMAL":49
    }
    style = {
        "BRIGHT":1,
        "DIM":2,
        "NORMAL":22,
        "RESETALL":0,
        "UNDERLINE":4,
        "BLINKSLOW":5,
        "BLINKRAPID":6,
        "ITALIC":3,
        "NEGATIVE":7
    }

def printColorido(texto, cor, back="NORMAL", style="NORMAL"):
    print("\033[{}m".format(Cor.fore.get(cor.upper())), end="")
    print("\033[{}m".format(Cor.back.get(back.upper())), end="")
    print("\033[{}m".format(Cor.style.get(style.upper())), end="")
    print(texto, end="")
    print("\033[{}m".format(Cor.style.get("RESETALL")), end="")

''' # para teste
printColorido("ola","RED","white","UNDERLINE")
printColorido(" mundo","blue","YELLOW")
print('\n')'''
