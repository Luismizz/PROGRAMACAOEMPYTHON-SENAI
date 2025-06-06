def atividade_1():
    try:
        n = int(input("Digite um Numero:"))
    except ValueError as erro:
        print(erro)
#atividade_1()
        
def atividade_2():
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        
        div = n1/n2
        print(div)
    except ZeroDivisionError as code:
       print(code)
    
#atividade_2()
       
def atividade_3():
    try:
        lista= [1,2,34,5]
        i = int(input("Digite um index: "))
        print(lista[i])
    except IndexError as erro:
        print(erro)
        
atividade_3()
        
    
    