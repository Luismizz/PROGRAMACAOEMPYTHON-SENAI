banco_dados = {}

nome1 = input("Nome: ")
idade1 = input("Idade: ")
senha1 = input("Senha: ")

nome2 = input("Nome:")
idade2 = input("Idade: ")
senha2 = input("Senha: ")

nome3 = input("Nome:")
idade3 = input("Idade: ")
senha3 = input("Senha: ")


banco_dados["nomes"] = [nome1, nome2, nome3]
banco_dados["idade"] = [idade1, idade2, idade3]
banco_dados["senha"] = [senha1, senha2, senha3]


print(banco_dados)

#Acesso:

login_nome= input("Digite seu nome")
senha_acesso = input("Digite sua Senha: ")

if login_nome in banco_dados["nomes"] and senha_acesso in banco_dados["senha"]:
    print("Seja bem vindo ao Sistema!")
    
    print("Escolha o Quarto: ", banco_dados["nomes"][0])
    quarto = ["", "Simples", "Duplo", "Luxo"]
    valores = ["", 100, 150, 250]
    print("Quatos: ", quarto)
    escolha = int(input("id 1 Simples | id 2 Duplo | id 3 Luxo"))
    qd = int(input("Quantidade de dias "))
    calculo = qd * valores[escolha]
    print("R$", calculo)
    print("Você escolheu o quarto ", quarto[escolha],  "Quantos dias", qd)
    print("Total a pagar R$", calculo)
    
    print("Escolha o Quarto: ", banco_dados["nomes"][1])
    quarto = ["", "Simples", "Duplo", "Luxo"]
    valores = ["", 100, 150, 250]
    print("Quatos: ", quarto)
    escolha = int(input("id 1 Simples | id 2 Duplo | id 3 Luxo"))
    qd = int(input("Quantidade de dias "))
    calculo = qd * valores[escolha]
    print("R$", calculo)
    print("Você escolheu o quarto ", quarto[escolha],  "Quantos dias", qd)
    print("Total a pagar R$", calculo)
    
    print("Escolha o Quarto: ", banco_dados["nomes"][2])
    quarto = ["", "Simples", "Duplo", "Luxo"]
    valores = ["", 100, 150, 250]
    print("Quatos: ", quarto)
    escolha = int(input("id 1 Simples | id 2 Duplo | id 3 Luxo"))
    qd = int(input("Quantidade de dias "))
    calculo = qd * valores[escolha]
    print("R$", calculo)
    print("Você escolheu o quarto ", quarto[escolha],  "Quantos dias", qd)
    print("Total a pagar R$", calculo)
    
    
    
else:
    print("Acesso Negado, Tente novamente!")