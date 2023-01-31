# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:48:04 2023

@author: marco
"""

import tkinter as tk
from tkinter import filedialog
#from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil 
import os

root = tk.Tk()
root.geometry("620x450")
root.title("Descargador automatico de Youtube")
canvas = tk.Canvas(root, width = 670, height = 450, bg='#d8c6ff')
canvas.pack()

imagen = tk.PhotoImage(file="youtube.png")
imagen = imagen.subsample(3,3)
canvas.create_image(200,75, image=imagen)

#----- Funciones -----
def SeleccionarRuta():
    ruta = filedialog.askdirectory()
    label_2.configure(text = ruta)
    
def DescargarArchivo():
    obtener_link = entry_1.get()
    user_path = label_2.cget("text")
    root.title('Descargando archivo...')
    video = YouTube(obtener_link).streams.get_highest_resolution().download()
    video_guardado = VideoFileClip(video)
    video_guardado.close()
    shutil.move(video, user_path)
    root.title('Descarga completa.')

    
def DescargaMP3():
    obtener_link = entry_1.get()
    user_path = label_2.cget("text")
    video = YouTube(obtener_link).streams.filter(only_audio=True).first()
    root.title('Descargando archivo...')
    out_file = video.download(output_path=user_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    root.title('Descarga completa.')

#----- Labels -----
label_1 = tk.Label(root, bg='#d8c6ff',
                   text="Introducir el link de descarga",
                   font=('Segoe UI',18))
label_1.place(x=40, y=145)

label_2 = tk.Label(root, bg='#d8c6ff', 
                   text="Ruta: ",
                   font=('Segoe UI',10))
label_2.place(x=40, y=280)


#----- Entries ------
entry_1 = tk.Entry(root, width=60, font=('Segoe UI',13))
entry_1.place(x=40, y=190)

#----- Botones ------
boton_1 = tk.Button(root, text="Seleccionar ruta", bg='#ccc9d1',
                    command = SeleccionarRuta,
                    font=('Segoe UI',13))
boton_1.place(x=40, y=235)

boton_2 = tk.Button(root, text="Descargar video", bg='#ccc9d1',
                    command = DescargarArchivo,
                    font=('Segoe UI',13))
boton_2.place(x=120, y=370)

boton_3 = tk.Button(root, text="Descargar mp3", bg='#ccc9d1',
                    command = DescargaMP3,
                    font=('Segoe UI',13))
boton_3.place(x=360, y=370)


root.mainloop()