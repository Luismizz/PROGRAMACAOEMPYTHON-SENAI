# QUARTOS COM LOOP


escolhas_quartos  = []
clientes =  []
meus_valores = []
quartos = ['SIMPLES','DUPLO','LUXO']
lista_precos =  [100.0,150.0,250.]
lista_desconto = [0.2,0.5,0.6]
print('''Sejam bem vindos,
Cadastre-se e
Escolha o ID  do quarto
SIMPLES(0),DUPLO(1),LUXO(2)''')


quantidade_hospede = int(input('Hopede - '))

for n in range(0,quantidade_hospede):
    nome = input('nome:')
    idade = int(input('idade:'))
    quarto = int(input('Escolha o ID quarto'))
    dias = int(input('quantidade de dias'))
    clientes.append(nome)
    escolhas_quartos.append(quarto)
    meus_valores.append(lista_precos[quarto])

    cal = (lista_precos[quarto] * dias)
    d = cal * lista_desconto[quarto]
    tp = cal - d
    

    print(clientes)
    print(escolhas_quartos)
    print(meus_valores)
    print(f'''Quartos escolhidos -  {escolhas_quartos}
                Valores escolhidos  -  {meus_valores}
                Cliente -  {nome}
                **********************************
                QUARTO - {quarto}
                DIAS - {dias}
                VALOR R$ {cal}
                DESCONTO - R${d}
                TOTAL A PAGAR -R$ {tp}
                ''')  
                
                
escolhas_quartos  = []
clientes =  []
meus_valores = []
quartos = ['SIMPLES','DUPLO','LUXO']
lista_precos =  [100.0,150.0,250.]
lista_desconto = [0.2,0.5,0.6]
print('''Sejam bem vindos,
Cadastre-se e
Escolha o ID  do quarto
SIMPLES(0),DUPLO(1),LUXO(2)''')

quantidade_hospede = int(input('Hopede - '))
for n in range(0,quantidade_hospede):
    nome = input('nome:')
    idade = int(input('idade:'))
    quarto = int(input('Escolha o ID quarto'))
    dias = int(input('quantidade de dias'))
    clientes.append(nome)
    escolhas_quartos.append(quarto)
    meus_valores.append(lista_precos[quarto])

    cal = (lista_precos[quarto] * dias)
    d = cal * lista_desconto[quarto]
    tp = cal - d
    
    print(clientes)
    print(escolhas_quartos)
    print(meus_valores)
    print(f'''Quartos escolhidos -  {escolhas_quartos}
                Valores escolhidos  -  {meus_valores}
                Cliente -  {nome}
                **********************************
                QUARTO - {quarto}
                DIAS - {dias}
                VALOR R$ {cal}
                DESCONTO - R${d}
                TOTAL A PAGAR -R$ {tp}
                ''')    