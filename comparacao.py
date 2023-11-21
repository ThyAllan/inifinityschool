from classes import Pessoa, Time, Jogador, Tecnico, Auxiliar, PreparadorFisico

def menu():
    print("1. Cadastrar Time")
    print("2. Cadastrar Jogador")
    print("3. Cadastrar Técnico")
    print("4. Cadastrar Auxiliar")
    print("5. Cadastrar Preparador Físico")
    print("6. Sair")
    return int(input("Escolha uma opção: "))

def main():
    times = []
    jogadores = []
    tecnicos = []
    auxiliares = []
    preparadores = []

    while True:
        opcao = menu()

        if opcao == 1:
            nome = input("Nome do time: ")
            cidade = input("Cidade:  ")
            mascote = input("Mascote: ")
            times.append(Time(nome, cidade, mascote))
        elif opcao == 2:
            nome = input("Nome do jogador: ")
            time = input("Time: Seleção ")
            numero_camisa = input("Número da camisa:")
            jogadores.append(Jogador(nome, time, numero_camisa))
        elif opcao == 3:
            nome = input("Nome do técnico:  ")
            time = input("Time: ")
            esquema_tatico = input("Esquema tático:  ")
            tecnicos.append(Tecnico(nome, time, esquema_tatico))
        elif opcao == 4:
            nome = input("Nome do auxiliar:")
            time = input("Time: ")
            esquema_tatico = input("Esquema tático: ")
            auxiliares.append(Auxiliar(nome, time, esquema_tatico))
        elif opcao == 5:
            nome = input("Nome do preparador físico:  ")
            time = input("Time: ")
            parte_elenco = input("Parte do elenco que prepara:")
            preparadores.append(PreparadorFisico(nome, time, parte_elenco))
        elif opcao == 6:
            break

if __name__ == "__main__":
    main()