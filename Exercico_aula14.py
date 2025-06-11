
letra = ""

match letra:
    case "a":
        print("Tem palavra")
    case _:
        print("string é vazia")

#--------------------------x-----------------

num = 12

match num:
    case num if num  > 10:
        print("O numero é maior que 10")
    case num if num < 10:
        print("O numero é menor que 10")
    case 10:
        print("O numero  é igual a 10")

#-----------------x-------------------------

idade = int(input("Digite sua Idade: "))

match idade:
    case idade if idade <= 12:
        print('Você é criança')
    case idade if  idade > 12 and idade <= 17:
        print('Você é Adolecente')
    case idade if idade > 17 and idade <= 35:
        print('Você é Adulto')
    case idade if idade > 35 and idade < 64:
        print('Você é Adulto')
    case idade if idade > 65:
        print('Você é Idoso')

    