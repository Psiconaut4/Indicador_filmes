from tkinter.ttk import *
from tkinter import *
from tkinter import ttk

# cores ---------------------------

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" #
co6 = "#03091f" # azul

# Criando janela --------------------

janela = Tk()
janela.title ("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use("clam")

# Frames ------------------------------

frameCima = Frame(janela, width=450, height=50, bg=co6, relief="flat",)
frameCima.grid(row=0, column=0)

frameAsk = Frame(janela, width=450, height=60, bg=co1, relief="solid",)
frameAsk.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co1, relief="solid",)
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=co1, relief="raised",)
frameBaixo.grid(row=3, column=0, sticky=NSEW)






janela.mainloop()