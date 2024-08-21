import tkinter
from tkinter import *

class cadastro:
    def __init__(self,master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("arial", "12")
        self.janela.pack()
        self.titulo = Label(self.janela, text="Informe os dados:")
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="idUsuario", font=self.fontePadrao, width=10)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 10
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2)
        self.buscar.pack(sid=LEFT)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "12")
        self.buscar["width"] = 14
        self.buscar.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontePadrao, width=10)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 25
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telLabel = Label(self.janela4, text="Telefone:", font=self.fontePadrao, width=10)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4)
        self.tel["width"] = 25
        self.tel["font"] = self.fontePadrao
        self.tel.pack(side=LEFT)

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.mailLabel = Label(self.janela5, text="E-mail:", font=self.fontePadrao, width=10)
        self.mailLabel.pack(side=LEFT)
        self.mail = Entry(self.janela5)
        self.mail["width"] = 25
        self.mail["font"] = self.fontePadrao
        self.mail.pack(side=LEFT)

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuLabel = Label(self.janela6, text="Usuário:", font=self.fontePadrao, width=10)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6)
        self.usu["width"] = 25
        self.usu["font"] = self.fontePadrao
        self.usu.pack(side=LEFT)

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontePadrao, width=10)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 25
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8)
        self.inserir.pack(sid=LEFT)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = ("Calibri", "12")
        self.inserir["width"] = 14
        self.inserir.pack()

        self.alterar = Button(self.janela8)
        self.alterar.pack(sid=LEFT)
        self.alterar["text"] = "Alterar"
        self.alterar["font"] = ("Calibri", "12")
        self.alterar["width"] = 14
        self.alterar.pack()

        self.excluir = Button(self.janela8)
        self.excluir.pack(sid=LEFT)
        self.excluir["text"] = "Excluir"
        self.excluir["font"] = ("Calibri", "12")
        self.excluir["width"] = 14
        self.excluir.pack()


root = Tk()
cadastro(root)
root.mainloop()