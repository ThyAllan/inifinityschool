def adicionar_nota():
    notas = []
    while True:
        nota = float(input("Digite uma nota (-1 para parar): "))
        if nota == -1:
            break
        notas.append(nota)
    return notas

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10!"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = adicionar_nota()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    print(f"Sua média é {media:.1f} e sua situação é {situacao}.")

if __name__ == "__main__":
    main()