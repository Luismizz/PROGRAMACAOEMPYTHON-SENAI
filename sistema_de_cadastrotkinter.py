import tkinter as tk
from tkinter import messagebox


def display():
    nome = nome_digitado.get()
    idade = int(idade_digitada.get())
    email = email_digitada.get()
    endereco = endereco_digitada.get()
    telefone = telefone_digitada.get()
    if nome and idade and email and endereco and telefone:
        MOSTRAR_NOME.config(text=nome)
        MOSTRAR_IDADE.config(text=idade)
        MOSTRAR_EMAIL.config(text=email)
        MOSTRAR_ENDERECO.config(text=endereco)
        MOSTRAR_TELEFONE.config(text=telefone)
    else:
       messagebox.showerror('isso é um erro', 'você não digitou nada')



janela  =  tk.Tk()
janela.title('SISTEMA DE CADASTRO ')
janela.geometry('500x500')

titulo_pag = tk.Label(janela,text = 'Cadastro de usuários', font=('arial',20))
titulo_pag.grid(row=0,column=0, padx=15, pady=10)


nome_ =  tk.Label(janela, text = 'Nome:', bg='yellow', font=('arial',10))
nome_.grid(row=1, column=0, pady=5)

nome_digitado =  tk.Entry(janela, font=('arial', 10))
nome_digitado.grid(row=1, column=1, padx=5, pady=5)


texto =  tk.Label(janela, text = 'Idade:', bg='yellow', font=('arial',10))
texto.grid(row=2, column=0, pady=5)

idade_digitada =  tk.Entry(janela, font=('arial', 10))
idade_digitada.grid(row=2, column=1, padx=5, pady=5)


email_ =  tk.Label(janela, text = 'E-mail:', bg='yellow', font=('arial',10))
email_.grid(row=3, column=0, pady=5)

email_digitada =  tk.Entry(janela, font=('arial', 10))
email_digitada.grid(row=3, column=1, padx=5, pady=5)


endereco_ =  tk.Label(janela, text = 'Endereço:', bg='yellow', font=('arial',10))
endereco_.grid(row=4, column=0, pady=5)

endereco_digitada =  tk.Entry(janela, font=('arial', 10))
endereco_digitada.grid(row=4, column=1, padx=5, pady=5)


telefone_ =  tk.Label(janela, text = 'Telefone:', bg='yellow', font=('arial',10))
telefone_.grid(row=5, column=0, pady=5)

telefone_digitada =  tk.Entry(janela, font=('arial', 10))
telefone_digitada.grid(row=5, column=1, padx=5, pady=5)


b_t = tk.Button(janela, text = 'clique aqui', font=('arial', 15), command=display)
b_t.grid(row=6, column=0, padx=5, pady=5)


MOSTRAR_NOME = tk.Label(janela, text = '',  font=('arial', 15))
MOSTRAR_NOME.grid(row=7, column=0, padx=5, pady=5)

MOSTRAR_IDADE = tk.Label(janela, text = '', font=('arial', 15))
MOSTRAR_IDADE.grid(row=8, column=0, padx=5, pady=5)

MOSTRAR_EMAIL = tk.Label(janela, text = '', font=('arial', 15))
MOSTRAR_EMAIL.grid(row=9, column=0, padx=5, pady=5)

MOSTRAR_ENDERECO= tk.Label(janela, text = '', font=('arial', 15))
MOSTRAR_ENDERECO.grid(row=10, column=0, padx=5, pady=5)

MOSTRAR_TELEFONE= tk.Label(janela, text = '', font=('arial', 15))
MOSTRAR_TELEFONE.grid(row=11, column=0, padx=5, pady=5)



janela.mainloop()