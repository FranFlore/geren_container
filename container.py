class Armazem:
    def __init__(armazem):
        armazem.pilhas = [[], [], [], []]

    def empilhar_container(armazem, codigo, posicao):
        if posicao < 3:
            for pilha in armazem.pilhas:
                if len(pilha) == posicao:
                    pilha.append(codigo)
                    empilhou = 1
                    return True
            
            posicao = posicao +1
            armazem.empilhar_container(codigo, posicao)
        
    def desempilhar_container(armazem, codigo):
        for pilha in armazem.pilhas:
            if pilha and pilha[-1] == codigo:
                pilha.pop()
                return True

    def codigo_duplicado(armazem, codigo):
        for pilha in armazem.pilhas:
            if codigo in pilha:
                return True
        return False

    def mostrar_armazem(armazem):
        for i, pilha in enumerate(armazem.pilhas):
            print(f"Local {i+1}: {pilha}")


if __name__ == "__main__":
    armazem = Armazem()

    while True:
        print("\n")
        print("1. Adicionar container")
        print("2. Remover container")
        print("3. Mostrar porto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Digite o código do container: ")
            if armazem.codigo_duplicado(codigo):
                print("Código inválido!")
            elif not armazem.empilhar_container(codigo, 0):
                print("Impossível empilhar!")
        elif opcao == "2":
            codigo = input("Digite o código do container a ser removido: ")
            if not armazem.codigo_duplicado(codigo):
                 print("Impossível desempilhar!")
            elif not armazem.desempilhar_container(codigo):
                print("Impossível desempilhar!")
        elif opcao == "3":
            armazem.mostrar_armazem()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")