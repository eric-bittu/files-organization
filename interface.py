import tkinter
from tkinter import messagebox
import main

janela = tkinter.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("300x150")
pasta_escolhida = tkinter.Entry(janela, width=30)
pasta_escolhida.pack(pady=20)

def definir_pasta():
    main.pasta = pasta_escolhida.get()
    main.origem = main.Path.home() / main.pasta
    main.organizar()
    messagebox.showinfo("Organizado a pasta", f"Arquivos organizados na pasta: {main.pasta}")
    

botao_organizar = tkinter.Button(janela, text="Organizar Arquivos", command=definir_pasta)
botao_organizar.pack(pady=10)

janela.mainloop()