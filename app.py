from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from io import BytesIO
import sys
import os
# importando função principal
from main import *


# Caminho base para o diretório onde os arquivos estão localizados
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS  # Diretório temporário criado pelo PyInstaller
else:
    base_path = os.path.abspath('.')  # Caminho local para desenvolvimento

# Caminho completo para as imagens
image_path_logo = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'logo.png')
image_path_neutro = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'neutro.png')
image_path_feliz = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'feliz.png')
image_path_amado = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'amado.png')
image_path_derretendo = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'derretendo.png')
image_path_medo = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'medo.png')
image_path_crying = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'crying.png')
image_path_raiva = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'raiva.png')
image_path_muitofeliz = os.path.join(base_path, 'Indicador_filmes', 'imagens', 'muitofeliz.png')

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
janela.title ("Psiconaut4 © Company ")
janela.geometry('460x560')
janela.configure(background=co7)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames ------------------------------

frameCima = Frame(janela, width=460, height=50, bg=co6, relief="flat",)
frameCima.grid(row=0, column=0,)

frameAsk = Frame(janela, width=450, height=60, bg=co7, relief="solid",)
frameAsk.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co7, relief="solid",)
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=co7, relief="raised",)
frameBaixo.grid(row=3, column=0, sticky=NSEW)

# Logo --------------------------------------

# abrindo imagem
img = Image.open(image_path_logo)
img = img.resize((40, 40))
img = ImageTk.PhotoImage(img)

logo = Label(frameCima, image=img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6)
logo.place(x=7, y=0)

name = Label(frameCima, text='Bot de recomendação de filmes', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
name.place(x=55, y=10)

l_linha = Label(frameCima, width=460, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# FrameAsk -----------------------------------------------------

ask = Label(frameAsk, text='Para melhorar os resultados das sugestões responda, Como você está se sentindo hoje?', width=45, height=2, wraplength=400, justify='center', compound=CENTER, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'), bg=co7, fg=co1)
ask.place(x=50, y=7)

l_linha = Label(frameAsk, width=450, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=55)

# funcao resultado -----------------------------------------------
def resultado(i):
    global capa_1, capa_2, capa_3

    # filmes sugeridos
    sugeridos = suggest_movies(i)

    titles = sugeridos[0]
    poster = sugeridos[1]
    data = sugeridos[2]
    votos = sugeridos[3]

    # limpando frame baixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()

    # ------------ Frame dos posters ---------------------
    #filme 1
    frame_1 = Frame(frameBaixo, width=150, height=400, bg=co7)
    frame_1.grid(row=0, column=0, sticky=NSEW, pady=5)

    nome = Label(frame_1, text=f'{titles[0]}', width=16, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=10, y=260)

    data_string_1 = f'{data[0]}'
    data_1 = datetime.strptime(data_string_1, "%Y-%m-%d")
    data_formatada = data_1.strftime('%B %Y')

    l_data_1 = Label(frame_1, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_data_1.place(x=5, y=310)

    l_voto_1 = Label(frame_1, text=f'Média de votos: {votos[0]}/10', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_voto_1.place(x=5, y=330)

    # Obtendo imagem
    response_1 = requests.get(f'{poster[0]}')
    img_url_1 = response_1.url
    response_1 = requests.get(img_url_1)
    imagem_1 = Image.open(BytesIO(response_1.content))

    capa_1 = imagem_1
    capa_1 = capa_1.resize((150,250))
    capa_1 = ImageTk.PhotoImage(capa_1)

    l_capa_1 = Label(frame_1, image=capa_1, padx=5, bg=co1, fg=co0)
    l_capa_1.place(x=5, y=0)

    # filme 2

    frame_2 = Frame(frameBaixo, width=150, height=400, bg=co7)
    frame_2.grid(row=0, column=1, sticky=NSEW, pady=5)

    nome = Label(frame_2, text=f'{titles[1]}', width=16, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=10, y=260)

    data_string_2 = f'{data[1]}'
    data_2 = datetime.strptime(data_string_2, "%Y-%m-%d")
    data_formatada = data_2.strftime('%B %Y')

    l_data_2 = Label(frame_2, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_data_2.place(x=5, y=310)

    l_voto_2 = Label(frame_2, text=f'Média de votos: {votos[1]}/10', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_voto_2.place(x=5, y=330)

    # Obtendo imagem
    response_2 = requests.get(f'{poster[1]}')
    img_url_2 = response_2.url
    response_2 = requests.get(img_url_2)
    imagem_2 = Image.open(BytesIO(response_2.content))

    capa_2 = imagem_2
    capa_2 = capa_2.resize((150,250))
    capa_2 = ImageTk.PhotoImage(capa_2)

    l_capa_2 = Label(frame_2, image=capa_2, padx=5, bg=co1, fg=co0)
    l_capa_2.place(x=5, y=0)

    # filme 3

    frame_3 = Frame(frameBaixo, width=150, height=400, bg=co7)
    frame_3.grid(row=0, column=2, sticky=NSEW, pady=5)

    nome = Label(frame_3, text=f'{titles[2]}', width=16, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=10, y=260)

    data_string_3 = f'{data[2]}'
    data_3 = datetime.strptime(data_string_3, "%Y-%m-%d")
    data_formatada = data_3.strftime('%B %Y')

    l_data_3 = Label(frame_3, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_data_3.place(x=3, y=310)

    l_voto_3 = Label(frame_3, text=f'Média de votos: {votos[2]}/10', anchor=NW, font=('Ivy 8'), bg=co7, fg=co1)
    l_voto_3.place(x=5, y=330)

    # Obtendo imagem
    response_3 = requests.get(f'{poster[2]}')
    img_url_3 = response_3.url
    response_3 = requests.get(img_url_3)
    imagem_3 = Image.open(BytesIO(response_3.content))

    capa_3 = imagem_3
    capa_3 = capa_3.resize((150,250))
    capa_3 = ImageTk.PhotoImage(capa_3)

    l_capa_2 = Label(frame_3, image=capa_3, padx=5, bg=co1, fg=co0)
    l_capa_2.place(x=5, y=0)



# FrameMeio ------------------------------------------------------
# botões

img_1 = Image.open(image_path_neutro)
img_1 = img_1.resize((28, 28))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frameMeio, command=lambda:resultado('meh'), image=img_1, compound=LEFT, width=100, text='Neutro', overrelief=RIDGE)
b_1.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)


img_2 = Image.open(image_path_feliz)
img_2 = img_2.resize((28, 28))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frameMeio, command=lambda:resultado('happy'), image=img_2, compound=LEFT, width=100, text='Feliz', overrelief=RIDGE)
b_2.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)


img_3 = Image.open(image_path_amado)
img_3 = img_3.resize((28, 28))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frameMeio, command=lambda:resultado('love'), image=img_3, compound=LEFT, width=100, text='Apaixonado', overrelief=RIDGE)
b_3.grid(row=0, column=2, sticky=NSEW, pady=2, padx=1)


img_4 = Image.open(image_path_derretendo)
img_4 = img_4.resize((28, 28))
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frameMeio, command=lambda:resultado('anxiety'), image=img_4, compound=LEFT, width=100, text='Ansioso', overrelief=RIDGE)
b_4.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2)


img_5 = Image.open(image_path_medo)
img_5 = img_5.resize((28, 28))
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frameMeio, command=lambda:resultado('horror'), image=img_5, compound=LEFT, width=100, text='Terror', overrelief=RIDGE)
b_5.grid(row=1, column=0, sticky=NSEW, pady=2, padx=1)


img_6 = Image.open(image_path_crying)
img_6 = img_6.resize((28, 28))
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frameMeio, command=lambda:resultado('sad'), image=img_6, compound=LEFT, width=100, text='Drama', overrelief=RIDGE)
b_6.grid(row=1, column=1, sticky=NSEW, pady=2, padx=1)


img_7 = Image.open(image_path_raiva)
img_7 = img_7.resize((28, 28))
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frameMeio, command=lambda:resultado('angry'), image=img_7, compound=LEFT, width=100, text='Raiva', overrelief=RIDGE)
b_7.grid(row=1, column=2, sticky=NSEW, pady=2, padx=1)


img_8 = Image.open(image_path_muitofeliz)
img_8 = img_8.resize((28, 28))
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frameMeio, command=lambda:resultado('very happy'), image=img_8, compound=LEFT, width=100, text='Comédia', overrelief=RIDGE)
b_8.grid(row=1, column=3, sticky=NSEW, pady=2, padx=1)

# Frame Baixo ---------------------------------------------------

#pyinstaller --onefile -- noconsole --icon=Indicador_filmes/imagens/pngwing.com.ico --add-data 'Indicador_filmes/imagens' Indicador_filmes/app.py 


janela.mainloop()