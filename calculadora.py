# calculadora (+ soma | - subtração | * multiplicação | / divisão )

def soma(n1,n2):
    print("Resultado", n1 + n2)
    print("-------------------x-----------------")
    
def subtracao(n1,n2):
    print("Resultado", n1 - n2)
    print("-------------------x-----------------")
    
def multiplicacao(n1,n2):
    print("Resultado", n1 * n2)
    print("-------------------x-----------------")
    
def divisao(n1,n2):
    print("Resultado", n1 / n2)
    print("-------------------x-----------------")
    
def calculadora():
    print("Calculadora:")
    n1 = float(input(" = "))
    op = input("Escolha a Operação + - * /")
    if op == "+":
        n2 = float(input(" = "))
        soma(n1,n2)
    elif op == "-":
        n2 =float(input(" = "))
        subtracao(n1,n2)
    elif op == "*":
        n2 =float(input(" = "))
        multiplicacao(n1,n2)
    elif op == "/":
        n2 =float(input(" = "))
        divisao(n1,n2)
    else:
        print("Digite algo valido")

while True:
    calculadora()
    
input("Digite enter para sair!")