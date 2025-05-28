# vazia
lista = []

#lista preenchida

lista_teste =[1,2,3,4,5,89,843,1212]

print(lista_teste[4])


lista_teste[5] = 100
print(lista_teste)

# append vai adicionar 1 dado no final
lista.append(10)
print(lista)

#varios dados no final da lista -> extend () +=()
lista.extend([10,20,30])
print(lista)

lista += ("a", "b")
print(lista)

#deletar dado del, remove() pop ()

lista.pop () #detela o ultimo numero

lista.pop(4) #deleta o indice que voce declarou
print(lista)

lista.remove(10)

del lista[2]

print(lista)

print(len(lista))

