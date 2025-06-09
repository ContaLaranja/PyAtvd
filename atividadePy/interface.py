from tkinter import *
from tkinter import messagebox

def adicionar_item():
    # Placeholder function for adding item
    messagebox.showinfo("Adicionar Item", "Próxima aula.")

def listar_estoque():
    # Placeholder function for listing stock
    messagebox.showinfo("Listar Estoque", "Próxima aula.")

def alterar_item():
    # Placeholder function for altering item
    messagebox.showinfo("Alterar Item", "Próxima aula.")

def excluir_item():
    # Placeholder function for excluding item
    messagebox.showinfo("Excluir Item", "Próxima aula.")

# Main window
menu_inicial = Tk()
menu_inicial.title("Sistema de Estoque")
menu_inicial.geometry("600x400")
menu_inicial['bg'] = "#000000"

# Labels
label_title = Label(menu_inicial, text="Sistema de Estoque", fg="white", font="Arial 24 bold", bg="#000000")
label_title.pack(pady=10)

# Buttons
btn_adicionar = Button(menu_inicial, text="Adicionar Item", bg="DarkGray", fg="white", font="Arial 16", command=adicionar_item)
btn_adicionar.pack(pady=5)

btn_listar = Button(menu_inicial, text="Listar Estoque", bg="DarkGray", fg="white", font="Arial 16", command=listar_estoque)
btn_listar.pack(pady=5)

btn_alterar = Button(menu_inicial, text="Alterar Item", bg="DarkGray", fg="white", font="Arial 16", command=alterar_item)
btn_alterar.pack(pady=5)

btn_excluir = Button(menu_inicial, text="Excluir Item", bg="DarkGray", fg="white", font="Arial 16", command=excluir_item)
btn_excluir.pack(pady=5)

btn_sair = Button(menu_inicial, text="Sair", bg="red", fg="white", font="Arial 16", command=menu_inicial.destroy)
btn_sair.pack(pady=20)

menu_inicial.mainloop()