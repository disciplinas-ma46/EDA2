def menu():
    import sys
    opcao = None
    print("==========================================");
    print("|         >>>>>>>>> Menu <<<<<<<<<       |");
    print("| 1 - Inserir valor                      |");
    print("| 2 - Remover valor                      |");
    print("| 3 - Carregar arvore de arquivo         |");
    print("| 0 - Sair                               |");
    print("==========================================");
    print("Sua opcao: ");
    opcao = sys.stdin.readline()
    # terminar, validat opcao para ser int
    return int(opcao);
