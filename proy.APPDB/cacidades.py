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

        self.cidLabel = Label(self.janela2, text="Cidade:", font=self.fontePadrao, width=10)
        self.cidLabel.pack(side=LEFT)
        self.cid = Entry(self.janela2)
        self.cid["width"] = 25
        self.cid["font"] = self.fontePadrao
        self.cid.pack(side=LEFT)

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.ufLabel = Label(self.janela3, text="UF:", font=self.fontePadrao, width=10)
        self.ufLabel.pack(side=LEFT)
        self.uf = Entry(self.janela3)
        self.uf["width"] = 25
        self.uf["font"] = self.fontePadrao
        self.uf.pack(side=LEFT)

root = Tk()
cadastro(root)
root.mainloop()