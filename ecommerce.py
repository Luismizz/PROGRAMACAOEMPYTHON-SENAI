alunos = {
    
'nomes':['Luís Miguel','Rud Junior','Brian fé','Karine Fernandes'],
'notas':[float(input('nota >')), float(input('nota >')), float(input('nota >')), float(input('nota >'))]

}

media_turma = (alunos['notas'][0] +  alunos['notas'][1] + alunos['notas'][2]+ alunos['notas'][3])/ len(alunos['notas'])

print('média', media_turma)



#Atividades fazendo ecommerce com dicionario

ecommerce = {
    
    'livros' : {
        
        'A':50.0,
        'B':70.0,
        'C':100.0
     
        },
    'eletronicos':{
        
        'Tablets':3000.0,
        'Fone':150.0,
             
        }
   
    
}

secao1 = input('Digite o seção 1')
secao2 = input('Digite o seção 2')

produto1 = input('Digite o produto 1')
produto2 = input('Digite o produto 2')

carrinho = [produto1, produto2]
valores =  [ecommerce[secao1][produto1],ecommerce[secao2][produto2]]
soma =  sum(valores)

print(carrinho)
print('R$', soma)

