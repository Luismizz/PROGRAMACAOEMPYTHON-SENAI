import random


chances = [3,2,1]

for u in chances:
    numero_ale = random.randint(1,11)
    print("Você tem apenas..", u, "chances")
    chute = int(input("Digite seu chute: "))

    if numero_ale == chute:
         print("Acertou em Cheio!!")
         break
    else:
         print("Errou Feio!")
else:
    print("Chances esgotadas!! Perdeu feio")