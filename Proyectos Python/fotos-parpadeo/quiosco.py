# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:41:59 2021

@author: ADM
"""

# APP: Fotos Quiosco
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import time
from datetime import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Foto - Guiño")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.close_app)
        
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        self.auxiliar = None
        self.gray = None
        self.img = ""
        
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 640, 480
        self.codec = cv2.VideoWriter_fourcc(*'MP4V')
        self.recording = False
        
        frm = tk.Frame(self)
        frm1 = tk.LabelFrame(frm, text="Instrucciones:")
        frm2 = tk.LabelFrame(frm, text="Preview")
                
        frm.pack(padx=15, pady=10)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)
    
        # -------------------------- frm 1 ----------------------------------       
        self.canvas = tk.Canvas(frm2,  width=self.width, height=self.height, 
                           borderwidth=1, relief=tk.SUNKEN)
        self.canvas.pack()
        
        # -------------------------- frm 2 ----------------------------------
        self.btnPhoto = tk.Label(frm1, text="Cuando aparezca que se le ha detectado la cara, un cuadrado rojo estará sobre su ojo derecho, parpadee para tomar la foto", width=100, command=None)
        
        self.btnPhoto.grid(row=0, column=0, padx=5, pady=5)
      
        # -------------------------- frm ---------------------------------- 
        self.statusBar = tk.Label(frm, text = "Detectando rostro", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
      
        self.cam_loop()
        
        
    def cam_loop(self):
        ret, frame = self.cap.read()
        
        if ret:
            
            self.gray = frame
            self.auxiliar = frame
        
            self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #frame = cv2.resize(frame, (self.width, self.height))A
            
            face = self.face_cascade.detectMultiScale(self.gray, 1.1,5)
            
            if len(face) != 0:
                self.statusBar.pack_forget()
                self.statusBar = tk.Label(self.master, text = "Rostro detectado", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
                self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
            else:
                self.statusBar.pack_forget()
                self.statusBar = tk.Label(self.master, text = "Detectando rostro...", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
                self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
            
            for x, y, w, h in face:
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                roi_gray = self.gray[y:y+h, x:x+w]
                #roi_color = self.auxiliar[y:y+h, x:x+w]
                
                eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.12, 18)
                cv2.putText(frame, "Cara Detectada", (x,y-12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
                
                #------ Código para ver cuadrados en los ojos -----
                #for sx, sy, sw, sh in eyes:
                    #cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
                
                if len(eyes) == 1:
                    time.sleep(1)
                    #self.statusBar.pack_forget()
                    #self.statusBar = tk.Label(self.master, text = "Tomando foto, espere 3 segundos", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
                    self.img = self.take_pic()
                    break
            frame = cv2.cvtColor(self.auxiliar, cv2.COLOR_BGR2RGB)            
            
        try:
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=photo, anchor='nw')
            self.canvas.image = photo
                    
        except:
            pass
        
        self.after(20, self.cam_loop)
             
    def close_app(self):
        if self.cap.isOpened():
            self.cap.release()
            
        self.destroy()
        
        
    def take_pic(self):
        # Capturar un frame
        ret, frame = self.cap.read()
        filename = f"{datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')}.jpg"
        
        if ret:
            cv2.imwrite(filename, frame)
            PhotoWindow(filename)
        
               
class PhotoWindow(tk.Toplevel):
    def __init__(self, filename):
        super().__init__()
        self.title("Foto")
        self.resizable(0, 0)
        self.grab_set()
        self.focus()
        width, height = 640, 480
        
        
        canvas = tk.Canvas(self, width=width+20, height=height+20, 
                           borderwidth=1, relief=tk.SUNKEN, bg='#f2f2f2')
        canvas.pack()
              
        
        cv_img = cv2.imread(filename, cv2.IMREAD_COLOR)
        cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img_re = cv2.resize(cv_img_rgb, (width, height))
        
        try:
            photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img_re))
            canvas.create_image(width//2 + 11, height//2 + 1, image=photo)
            canvas.image = photo
        except:
            pass
        
        

        
App().mainloop()