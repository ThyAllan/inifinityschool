somatorio = 0
maior = 0
menor = 0

qtn= int( input("Quantas Notas serão calculadas?"))
#loop geral da digitação (entrada de dados) e processamento:
for contador in range(qtn):
    nota = (-1) #necessário para entrar no loop pela primeira vez
    #loop de validação dos valores das notas: 
    while (nota<0) or (nota>10):
        nota = float(input(f"Digite a nota {contador+1}: "))
        
        somatorio += nota 
        if (nota>=maior): #descoberta da maior nota
            maior = nota 
            if (nota<=menor): #descoberta da menor nota 
                menor = nota
                
               
                
            print(f"Maior nota: {maior}, Menor nota:")