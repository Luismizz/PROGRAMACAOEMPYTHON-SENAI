#Exercicio 1 -  Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
numero = 4

print(numero)
print(numero**2)

#Exercicio 2 -  Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
nome = (input("Digite seu nome: "))
sobrenome = (input("Digite seu Sobrenome "))
print(nome, "" + sobrenome)

#Exercicio 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite io segundo numero: "))
print(str(num1))
print(str(num2))

# Exercicio 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
palavra = "Python"
print (palavra, "5")

#Exercicio 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.
frase = "Decisões decidem destinos"
palavra_do_usuario = (input("Digite uma frase que combine com a Frase: "))
print(frase, "" + palavra_do_usuario)