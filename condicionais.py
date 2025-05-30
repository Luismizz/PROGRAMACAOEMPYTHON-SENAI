idade  =  int(input('Idade: '))

# condicional simples *** 
if idade >= 16:
   print('Você pode votar')

if idade <16:
    print('Não pode votar')

if idade >=65:
    print('Não precisa votar')
    
#----------------x----------------
    
idade =  int(input('Digite sua idade >>'))
titulo_eleitor  =  input('Possui Título de eleitor? s ou n >> ')

if idade >= 16 and titulo_eleitor == 's':
    print('\nPode votar')
else:
    print('Você não pode Votar')
    
    
#--------------x-------------------

ingresso_spfc = input("Ingresso com Desconto? sim/não")

if ingresso_spfc == "sim" or ingresso_spfc == "não":
    print("Acesso Autorizado! Bom jogo")
    
else:
    print("Acesso não Autorizado")
    
#------------------x------------------------

idade = int(input("idade: "))

if idade <= 12:
    print("Criança")
elif idade >12 and idade <=14:
    print("Pré-Adolenscente")
elif idade >=15 and idade <= 17:
    print("Adolescente")
elif idade >=18 and idade <= 25:
    print("Jovem")
elif idade >25 and idade <= 64:
    print("Adulto")
else:
    print("Idoso(a)")