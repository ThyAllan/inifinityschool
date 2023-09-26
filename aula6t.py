#checar: https://medium.com/@jonathannascimento1986eb/programando-o-jogo-jokenp%C3%B4-em-python-46306e6b7dab


#Importando Modulo Random:
from random import randint
#Importar o modulo time para cadenciar o jogo
from time import sleep
#Definindo em uma variavel:
opcoes = ("Pedra", "Papel", "Tesoura")
computador = randint( 0, 2)
print( '''Suas opções: 
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      
      
      
      ''')
jogador = int(input("Qual sua escolha?"))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(2)
print('-=' * 11)

#Resultado das escolhas: (SHIFT + ALT) (CTRL + ALT + SHIFT)
 

print(f'computador jogou:{opcoes[computador]}')
print(f'Jogador jogou: {opcoes[jogador]}')
print('-=' * 11)


#Resultados:
if computador == 0: # Computador jogou pedra
    if jogador == 0: 
        print('Empate')
        
elif jogador == 1:
    print('Jogador é o VENCEDOR!!')
    
elif jogador ==2:
    print("Computador VENCEU!!")
    
else: print("Jogada Inválida")