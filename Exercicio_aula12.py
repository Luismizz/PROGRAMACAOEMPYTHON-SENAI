# atividade 1
import random

def ale_atorio():
    aleatorio = random.randint(5,10)
    print(aleatorio)
ale_atorio()

#atividade 2
    
def num_alea3():
    ale_1 = random.randint(1,10)
    ale_2 = random.randint(1,10)
    ale_3 = random.randint(1,10)
    
    print(ale_1, ale_2, ale_3)
num_alea3()

#Atividade 3
def ale_range(): 
    var = random.randrange(10,30)
    print(var) 
    
ale_range()

#Atividade 4
    
def contagem_reg():
    for i in range(10,0,-1):
         print(i)
    print("Fogo!")
    
contagem_reg()
    
#Atividade 5
    
def soma_pares():
    n = int(input("Insira um numero Inteiro: "))
    l = []
    for i in range(0,n,2):
        l.append(i)
        soma = sum(l)
    print(soma)
soma_pares()

#Atividade 6

def tab_multi():
    n = int(input("Digite o multiplicador da Tabuada: "))
    for i in range(0,11): 
        calculo = i * n
        print(n, "x", i, "=", calculo)
tab_multi()

#Atividade 7

def num_impar():
    for i in range(99,0,-2):
        print(i)
num_impar()