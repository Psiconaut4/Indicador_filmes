from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# cores ---------------------------

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" #
co6 = "#03091f" # azul
co7 = "#380036" # Psiconaut4

# Criando janela --------------------

janela = Tk()
janela.title ("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

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

# Logo --------------------------------------

# abrindo imagem
img = Image.open('Indicador_filmes/imagens/logo.png')
img = img.resize((40, 40))
img = ImageTk.PhotoImage(img)

logo = Label(frameCima, image=img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6)
logo.place(x=7, y=0)

name = Label(frameCima, text='Bot de recomendação de filmes', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
name.place(x=55, y=10)

l_linha = Label(frameCima, width=450, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# FrameAsk -----------------------------------------------------

ask = Label(frameAsk, text='Para melhorar os resultados das sugestões responda, Como você está se sentindo hoje?', width=45, height=2, wraplength=400, justify='center', compound=CENTER, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'), bg=co1, fg=co0)
ask.place(x=50, y=7)

l_linha = Label(frameAsk, width=450, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=55)

# FrameMeio ------------------------------------------------------
# botões

img_1 = Image.open('Indicador_filmes/imagens/neutro.png')
img_1 = img_1.resize((28, 28))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frameMeio, image=img_1, compound=LEFT, width=100, text='Neutro', overrelief=RIDGE)
b_1.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)


img_2 = Image.open('Indicador_filmes/imagens/feliz.png')
img_2 = img_2.resize((28, 28))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frameMeio, image=img_2, compound=LEFT, width=100, text='Feliz', overrelief=RIDGE)
b_2.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)


img_3 = Image.open('Indicador_filmes/imagens/amado.png')
img_3 = img_3.resize((28, 28))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frameMeio, image=img_3, compound=LEFT, width=100, text='Apaixonado', overrelief=RIDGE)
b_3.grid(row=0, column=2, sticky=NSEW, pady=2, padx=1)


img_4 = Image.open('Indicador_filmes/imagens/derretendo.png')
img_4 = img_4.resize((28, 28))
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frameMeio, image=img_4, compound=LEFT, width=100, text='Ansioso', overrelief=RIDGE)
b_4.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2)


img_5 = Image.open('Indicador_filmes/imagens/medo.png')
img_5 = img_5.resize((28, 28))
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frameMeio, image=img_5, compound=LEFT, width=100, text='Terror', overrelief=RIDGE)
b_5.grid(row=1, column=0, sticky=NSEW, pady=2, padx=1)


img_6 = Image.open('Indicador_filmes/imagens/crying.png')
img_6 = img_6.resize((28, 28))
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frameMeio, image=img_6, compound=LEFT, width=100, text='Drama', overrelief=RIDGE)
b_6.grid(row=1, column=1, sticky=NSEW, pady=2, padx=1)


img_7 = Image.open('Indicador_filmes/imagens/raiva.png')
img_7 = img_7.resize((28, 28))
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frameMeio, image=img_7, compound=LEFT, width=100, text='Raiva', overrelief=RIDGE)
b_7.grid(row=1, column=2, sticky=NSEW, pady=2, padx=1)


img_8 = Image.open('Indicador_filmes/imagens/muitofeliz.png')
img_8 = img_8.resize((28, 28))
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frameMeio, image=img_8, compound=LEFT, width=100, text='Comédia', overrelief=RIDGE)
b_8.grid(row=1, column=3, sticky=NSEW, pady=2, padx=1)


janela.mainloop()