# Variaveis locais - criadas e usadas dentro da função
# Variaveis Globais - Criadas fora da função
#Globais podem ser usadas em Qualquer Lugar

# Variavel Global
nome = input("Nome> ")

def mostrar_dadod():
    print("Seja Bem Vindo(a)", nome)
    
mostrar_dadod()
print(nome)

def teste():
    print("Hello", nome)
    
teste()

#-----------------x--------------------
# Variavel locais
def teste2():
    nome2 = input("Teste: ")
    print("Isso é um ", nome2)
    
    
teste2()
print(nome2)
    
    
