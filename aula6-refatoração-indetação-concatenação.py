#indentação em python - organizar o código py
#indentação é um tipo de organização dos códigos
#variavel precisa estar encostada na borda
#quando não estiver dentro de nenhum escopo

x=10

#quando estiver dentro de um escopo
#precisa te pelo menos 1 espaço
#O padrão são 4 espaços

if x == 10:
    print(x)
    
    
# --------------------

#Concatenação
nome = "Maria"
print("Olá, seja bem vinda", nome)
print("Olá, seja bem vinda" + ""+ nome)
print("Olá, seja bem vinda {}". format(nome))
print("Olá, seja bem vinda %s"% (nome))
print(f"Olá, seja bem vinda {nome}")


#-----------------------

# refatoração = melhorar o codigo

x = "Julio"
y= "Cesar"

print("Hello", x, y)

nome = "Julio"
sobrenome = "Cesar"

print("Hello", nome, sobrenome)