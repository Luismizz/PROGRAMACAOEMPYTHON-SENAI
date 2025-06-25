# Requsito:
# tkinter - interface grafica
# Sqlite3 - Bancos de Dados
# TTk - Submodulo do tkinter
# MessageBox - Biblioteca que cria uma caixa de dialogo
# Python puro

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conectar():
    return sqlite3.connect("teste.db")

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            cpf INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# CREATE - CRIAR
def inserir_usuario():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    email = entry_email.get()
    if cpf and nome and email:
        try:
            conn = conectar()
            c = conn.cursor()
            c.execute("INSERT INTO usuarios (cpf, nome, email) VALUES (?, ?, ?)", (cpf, nome, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("AVISO", "DADOS INSERIDOS")
            mostrar_usuario()
        except sqlite3.IntegrityError:
            messagebox.showerror("ERRO", "CPF já existe.")
    else:
        messagebox.showerror("ERRO", "PREENCHA TODOS OS CAMPOS")

# READ - LER
def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    for user in usuarios:
        tree.insert("", "end", values=(user[0], user[1], user[2]))
    conn.close()

# DELETE - DELETAR
def delete_usuario():
    dados_del = tree.selection()
    if dados_del:
        user_cpf = tree.item(dados_del[0])["values"][0]
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM usuarios WHERE cpf = ?", (user_cpf,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO')
        mostrar_usuario()
    else:
        messagebox.showerror("ERRO", "SELECIONE UM ITEM")

# UPDATE - ATUALIZAR
def editar():
    selecao = tree.selection()
    if selecao:
        user_cpf = tree.item(selecao[0])["values"][0]
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            c.execute("UPDATE usuarios SET nome = ?, email = ? WHERE cpf = ?", (novo_nome, novo_email, user_cpf))
            conn.commit()
            conn.close()
            messagebox.showinfo("EDIÇÃO", "DADOS EDITADOS")
            mostrar_usuario()
        else:
            messagebox.showerror("ERRO", "PREENCHA TODOS OS CAMPOS")
    else:
        messagebox.showwarning('', 'SELECIONE UM ITEM')

# Interface gráfica
janela = tk.Tk()
janela.configure(bg="#D3D3D3")
janela.title('CRUD')
janela.geometry('700x500')

TITULO = tk.Label(janela, text="SISTEMA DE CADASTRO", fg="#808080", bg="#D3D3D3", font=("roboto", 20, "bold"))
TITULO.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

label_cpf = tk.Label(janela, text="CPF: ", fg="white", bg="#4B0082", font=("arial", 10))
label_cpf.grid(row=1, column=0, padx=10, pady=5)
entry_cpf = tk.Entry(janela, font=("arial", 15))
entry_cpf.grid(row=1, column=1, padx=10, pady=5)

label_nome = tk.Label(janela, text="NOME: ", fg="white", bg="#4B0082", font=("arial", 10))
label_nome.grid(row=2, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela, font=("arial", 15))
entry_nome.grid(row=2, column=1, padx=10, pady=5)

label_email = tk.Label(janela, text="E-MAIL: ", fg="white", bg="#4B0082", font=("arial", 10))
label_email.grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(janela, font=("arial", 15))
entry_email.grid(row=3, column=1, padx=10, pady=5)

btn_salva = tk.Button(janela, text="Salvar", font=("arial", 12), command=inserir_usuario)
btn_salva.grid(row=4, column=0, padx=10, pady=10)

btn_editar = tk.Button(janela, text="Editar", font=("arial", 12), command=editar)
btn_editar.grid(row=4, column=1, padx=10, pady=10)

btn_excluir = tk.Button(janela, text="Excluir", font=("arial", 12), command=delete_usuario)
btn_excluir.grid(row=4, column=2, padx=10, pady=10)

columns = ("CPF", "NOME", "E-MAIL")
tree = ttk.Treeview(janela, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)


criar_tabela()
mostrar_usuario()
janela.mainloop()






# CREATE =  CRIAR 
# READ   =  LER
# UPDATE = ATUALIZAR 
# DELETE =  DELETAR
