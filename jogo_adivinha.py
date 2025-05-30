import random
numero_da_sorte = random.randint(1,1000)
meu_numero = int(input("Digite seu nume da sorte: "))

if numero_da_sorte == meu_numero:
    print("Você é Sortudo(a), Acertou em cheio * . *", "O Nº é:", numero_da_sorte)
else:
  print("Você errou feio, não sabe escolher:p O Nº é", numero_da_sorte) 
                 
                