# Exercicio 1
usuario = int(input("Digite um Numero: "))

if usuario >= 0:
    print("Esse numero é Positivo")
if usuario <= 0:
    print("Esse Numero é negativo: ")
if usuario == 0:
    print("Esse numero é Igual a Zero")

# Exercicio 2
idade = int(input("\nDigite a sua Idade: "))

if idade >= 16:
    print("Você Pode Votar!")
else:
    print("Você não Pode Votar!")
    
# Exercicio 3
numero = 4

if numero % 2 == 0:
    print("\nO número é par.")
else:
    print("\nO número é impar.")
    
# Exercicio 4
print("\nQue numeros os triangulos tem?")

lado1 = int(input("\nDigite o Numero do Primeiro lado: "))
lado2 = int(input("Digite o Numero do Segundo lado: "))
lado3 = int(input("Digite o Numero do Terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Equilatero")
if lado1 == lado2 != lado3:
    print("isósceles")
if lado1 != lado2 == lado3:
    print("isósceles")
if lado1 != lado2 != lado3:
    print("Escaleno")
    
# Exericio 5
num1 = 15

if num1 % 5 == 0 or num1 % 7 == 0:
    print("\nEsse numero é multiplo de 5 ou de 7")
else:
    print("\nEle não é Multiplo de 5 ou 7")
    
# Exercicio 6
num_positivo = 17

if num_positivo > 10:
    print("\nO Numero é Posiivo e Maior que 10")
else:
    print("\nO Numero e Menor que 10")
    
# Exercicio 7
num_div = 28

if num_div % 3 == 0 or num_div % 5 == 0:
    print("\nEsse Numero é divisivel a 3 ou 5")
else:
    print("\nNão é Divisivel")
        