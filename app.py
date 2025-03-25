import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

#Função para abrir a imagem
def abrir_imagem():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if caminho:
        carregar_imagem(caminho)

#Função para carregar a imagem
def carregar_imagem(caminho):
    global imagemOriginal, img, imagemLabel
    imagemOriginal = cv2.imread(caminho)
    imagemOriginal_pil = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2RGB)
    imagemOriginal_pil = Image.fromarray(imagemOriginal_pil)
    imagemOriginal_pil.thumbnail((400, 400))
    img = ImageTk.PhotoImage(imagemOriginal_pil)
    imagemLabel.config(image=img)
    imagemLabel.image = img

#Função para dar Blur nas imagens
def blurIMG():
    global imagemOriginal, img
    imagemAtual = imagemOriginal.copy()
    imagemAtual = cv2.GaussianBlur(imagemAtual, (15, 15), 0)
    
    imagemAtualRGB = cv2.cvtColor(imagemAtual, cv2.COLOR_BGR2RGB)
    
    imagemAtualPill = Image.fromarray(imagemAtualRGB)
    imagemAtualPill.thumbnail((400, 400))
  
    img = ImageTk.PhotoImage(imagemAtualPill)
    imagemLabel.config(image=img)
    imagemLabel.image = img

#Função para realçar detalhes e bordas das imagens
def sharpedIMG():
    global imagemOriginal, img
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    imagemAtual = imagemOriginal.copy()
    imagemAtual = cv2.filter2D(imagemAtual, -1, kernel)
  
    imagemAtualRGB = cv2.cvtColor(imagemAtual, cv2.COLOR_BGR2RGB)
    
    imagemAtualPill = Image.fromarray(imagemAtualRGB)
    imagemAtualPill.thumbnail((400, 400))
    
    img = ImageTk.PhotoImage(imagemAtualPill)
    imagemLabel.config(image=img)
    imagemLabel.image = img

#Função para rotacionar a imagem
def rotacionarIMG():
    global imagemOriginal, img
    imagemAtual = imagemOriginal.copy()
    
    (h, w) = imagemAtual.shape[:2]
    centro = (w // 2, h // 2)
    matriz_rotacao = cv2.getRotationMatrix2D(centro, 45, 1.0)
    
    IMGrotacionada = cv2.warpAffine(imagemAtual, matriz_rotacao, (w, h))
    
    IMGRotacionadaRGB = cv2.cvtColor(IMGrotacionada, cv2.COLOR_BGR2RGB)
    
    IMGRotacionadaPill = Image.fromarray(IMGRotacionadaRGB)
    IMGRotacionadaPill.thumbnail((400, 400))
    
    img = ImageTk.PhotoImage(IMGRotacionadaPill)
    imagemLabel.config(image=img)
    imagemLabel.image = img

tela = TkinterDnD.Tk()
tela.title("Importar e Exibir Imagem")
tela.geometry("500x500")

tela.drop_target_register(DND_FILES)

btn_abrir = tk.Button(tela, text="Escolher Imagem", command=abrir_imagem)
btn_abrir.pack(pady=10)

imagemLabel = tk.Label(tela)
imagemLabel.pack()

frame_botoes = tk.Frame(tela)
frame_botoes.pack(pady=10)

btn1 = tk.Button(frame_botoes, text="Blur", command=blurIMG)
btn1.pack(side=tk.LEFT, padx=5)

btn2 = tk.Button(frame_botoes, text="Sharped", command=sharpedIMG)
btn2.pack(side=tk.LEFT, padx=5)

btn3 = tk.Button(frame_botoes, text="Rotacionar", command=rotacionarIMG)
btn3.pack(side=tk.LEFT, padx=5)

tela.mainloop()