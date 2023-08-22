n1=float(input("Digite um número aqui:"))
n2=float(input("Digite um número aqui:"))

if n1>n2:
    print(" O {n1} é maior do que o {n2}")
    
else: print(" O {n2} é maior do que o {n1}")

#**********************VOGAL E CONSOANTES*************************
letra= input("Digite Letra:").strip().upper()
if letra in "aeiou":
    print(f"{letra}é uma vogal")
elif letra in ("qwrtypsdfghjklçzxcvbnm")
    print(f"{letra}" é uma consoante)