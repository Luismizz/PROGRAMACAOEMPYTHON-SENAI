with open('exemplo.txt', 'w') as f:
    f.write('olá como vc,tá.')
with open('exemplo.txt', 'r') as f:
    conteudo = f.read()
    print('Conteúdo do arquivo:', conteudo)
#2
import os
os.makedirs('C:/Users/marco/python aula 13/meu_diretorio', exist_ok=True)
print("Diretório criado.")
#3
import os
os.rename("meu_diretorio",'diretorio_renomeado')
#4
import os
with os.scandir('diretorio_renomeado') as entrada:
    for item in entrada:
        if item.is_file():
            print(f'intem encontrado: {item.name}')
#5
import shutil
os.makedirs('copia')
shutil.copy('exemplo.txt', 'copia/exemplo_copiado.txt')
print("Arquivo copiado com sucesso.")
#5
import os
import shutil
os.remove('copia/exemplo_copiado.txt')
shutil.rmtree('copia')
shutil.rmtree('diretorio_renomeado')
os.remove('exemplo.txt')
print("tudo foi apagado removidos.")