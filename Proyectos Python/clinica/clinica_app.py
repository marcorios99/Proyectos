# -*- coding: utf-8 -*-
#Marco Rios, u202017158 
import tkinter as tk
import tkinter.ttk as ttk
from db_clinica import Database
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow:
    def __init__(self, master):
        # Definicion de la Ventana Principal
        self.master = master
        self.master.title("Clinica Peso Feliz")
        self.master.resizable(0, 0)
        
        self.db = Database()
        
        style = ttk.Style()
        style.theme_use('default')
        
        style.configure("Treeview",)
        
        frm = tk.Frame(self.master)
        frm.pack(padx=10, pady=10)
        
        frm1 = tk.LabelFrame(frm, text="Medicos")
        frm1.pack(side=tk.LEFT, padx=10, pady=10)
        frm2 = tk.LabelFrame(frm, text="Data Pacientes")
        frm2.pack(side=tk.LEFT, padx=10, pady=10)
        
        # -------------------------- frm1 ------------------------------
        # Tabla para el registro de los Medicos
        self.tabMedicos = ttk.Treeview(frm1, columns=(1, 2))
        self.tabMedicos.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.tabMedicos.heading('#0', text= "ID")
        self.tabMedicos.heading('#1', text= "Nombre")
        self.tabMedicos.heading('#2', text= "Apellido")
        
        self.tabMedicos.column('#0', width=60, minwidth=100, stretch=tk.NO)
        self.tabMedicos.column('#1', width=100, minwidth=100, stretch=tk.NO)
        self.tabMedicos.column('#2', width=100, minwidth=100, stretch=tk.NO)
       
                
        for item in self.db.listar_medicos():
            self.tabMedicos.insert("", tk.END, text = item[0], values = item[1:])
        
        self.tabMedicos.bind("<<TreeviewSelect>>", self.update_data_patients)
        # NOTA: Al hacer click a un medico debe llamar al metodo self.update_data_patients
        
        # -------------------------- frm2 ------------------------------ 
        # Tabla con el registro de los Pacientes + Scrollbar Vertical
        self.scrY = tk.Scrollbar(frm2, orient='vertical')
        self.tabPacientes = ttk.Treeview(frm2, columns=(1, 2, 3, 4, 5), 
                                         yscrollcommand=self.scrY.set,
                                         selectmode='browse')
        self.scrY.configure(command=self.tabPacientes.yview)
        
        self.tabPacientes.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.tabPacientes.heading('#0', text= "ID")
        self.tabPacientes.heading('#1', text= "Apellido")
        self.tabPacientes.heading('#2', text= "Nombre")
        self.tabPacientes.heading('#3', text= "Altura")
        self.tabPacientes.heading('#4', text= "Edad")
        self.tabPacientes.heading('#5', text= "Sexo")
        
        self.tabPacientes.column('#0', width=120, minwidth=30, stretch=tk.NO)
        self.tabPacientes.column('#1', width=120, minwidth=150, stretch=tk.NO)
        self.tabPacientes.column('#2', width=120, minwidth=80, stretch=tk.NO)
        self.tabPacientes.column('#3', width=120, minwidth=80, stretch=tk.NO)
        self.tabPacientes.column('#4', width=80, minwidth=80, stretch=tk.NO)
        self.tabPacientes.column('#5', width=80, minwidth=80, stretch=tk.NO)
       
        
        self.scrY.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        
        # NOTA: Al hacer click a un paciente debe llamar a self.open_graph_window
        self.tabPacientes.bind("<<TreeviewSelect>>", self.open_graph_window)
        
        # ------------------------ statusbar ---------------------------
        self.statusbar = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tabMedicos.bind("<Enter>", lambda x: self.update_statusbar("Haga click para ver los pacientes asigandos al medico"))
        self.tabMedicos.bind("<Leave>", lambda x: self.update_statusbar(""))
        self.tabPacientes.bind("<Enter>", lambda x: self.update_statusbar("Haga click para ver el registro de peso del paciente"))
        self.tabPacientes.bind("<Leave>", lambda x: self.update_statusbar(""))


    def update_statusbar(self, message):
        # Actualiza los mensajes en el statusbar
        self.statusbar.config(text=message)
       
        
    def update_data_patients(self, event):
        # Carga con datos la tabla de pacientes al seleccionar un medico
        idx = self.tabMedicos.selection()
        pacient = self.tabMedicos.item(idx)['text']
        
        self.tabPacientes.delete(*self.tabPacientes.get_children())
        
        for idx,paciente in enumerate(self.db.listar_pacientes_medico(pacient)):
            self.tabPacientes.insert("", tk.END, text=paciente[1], values=paciente[2:])
            
    
    def open_graph_window(self, event):
        # Abre la ventana secundaria con el grafico de peso
        window = tk.Toplevel(self.master)
        idx = self.tabPacientes.selection()
        id_pac = self.tabPacientes.item(idx)['text']
        GraphWindow(window, id_pac)
    
    
class GraphWindow:
    def __init__(self, master, id_pac):
        # Definicion de la ventana grafica
        # (requiere id_pac para cargar los datos de un paciente)
        self.master = master
        self.master.title("Reporte Gráfico")
        self.master.geometry("400x300")
        
        self.db = Database()
        
        frm = tk.Frame(self.master)
        frm.pack()
        
        self.nombres = self.db.nombre_paciente(id_pac)
        self.pesos = self.db.data_peso(id_pac)
        self.pesos_minimos = round(min(self.pesos)-20)
        self.pesos_maximos = round(min(self.pesos)+30)
        
        # ------------------ Figura de Matplotlib -----------------------------
        self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor="#F0F0ED")
        self.ax.grid(linestyle=":")
        self.line = self.ax.plot(self.pesos, '-s')
        self.ax.set_ylim(self.pesos_minimos, self.pesos_maximos)
        self.ax.set_title(f"Paciente - {self.nombres[0:]}")
        self.ax.set_xlim(0, len(self.pesos)+2)
        self.ax.set_xticklabels([0,2,4,6,8,10,12,14,16,18])
        #self.ax.set_yticklabels([i for i in range(self.pesos_minimos,self.pesos_maximos)])    
        
        self.ax.set_xlabel("Semana")
        self.ax.set_ylabel("Peso [Kg]")
        self.graph = FigureCanvasTkAgg(self.fig, master=frm)
        self.graph.get_tk_widget().pack(expand=True, fill=tk.X)
        
        


root = tk.Tk()
app = MainWindow(root)
root.mainloop()
