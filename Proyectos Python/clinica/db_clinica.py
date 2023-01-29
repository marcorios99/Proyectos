# -*- coding: utf-8 -*-
#Marco Rios, u202017158 
import sqlite3

class Database:
    datafile = "clinica.db"
    def __init__(self):
        # Se habilita la conexion con la dB
        self.conn = sqlite3.connect(Database.datafile)
        self.cur = self.conn.cursor()
        
        
    def __del__(self):
        # Se cierra la conexion con la dB
        self.conn.close()
        
        
    def listar_medicos(self):
        # Retorna una lista de tuplas con la informacion de los medicos
        # con el formato [(med_id, nombre, apellido), ...]
        #
        # Se utiliza para llenar la informacion de la tabla tabMedicos
        sql = """SELECT medicos.med_id, medicos.nombre, medicos.apellido FROM medicos"""  
        return [(item[0],item[1],item[2]) for  item in self.cur.execute(sql)]
    
    
    def listar_pacientes_medico(self, med_id):
        # Retorna una lista de tuplas con la información de un paciente que se 
        # encuentra asignado a un medico (segun el med_id) con el formato
        # [(pac_id, apellido, nombre, altura, edad, sexo), ...], ordenado 
        # alfabeticamente por apellido
        #
        # Se utiliza para llenar la informacion de la tabla tabPacientes
        sql = """SELECT medicos.med_id, pacientes.pac_id, pacientes.apellido, pacientes.nombre, pacientes.altura, pacientes.edad, pacientes.sexo FROM medicos
                JOIN medico_paciente
                JOIN pacientes
                ON medicos.med_id = medico_paciente.med_id
                   AND  medico_paciente.pac_id = pacientes.pac_id
                   WHERE medicos.med_id = ?"""
        
        return [(item[0], item[1], item[2], item[3], item[4], item[5], item[6]) for  item in self.cur.execute(sql,(med_id,))]   
    
    def nombre_paciente(self, id_pac):
        # Retorna una string con el nombre del paciente con el formato "apellido, nombre"
        #
        # Se utiliza para el titulo del gráfico
        sql = """SELECT pacientes.pac_id, pacientes.nombre, pacientes.apellido FROM pacientes
                WHERE pacientes.pac_id = ?"""
        
        results = self.cur.execute(sql,(id_pac,))
        for item in results:
            a = "{}, {}".format(item[1],item[2])
        
        return a
    
    
    def data_peso(self, pac_id):
        # Retorna una lista con los pesos registrados de un paciente en el 
        # historial de pesos: [peso1, peso2, ...]
        #
        # Se utiliza para el reporte gráfico
        sql = """SELECT historial_pesos.pac_id, historial_pesos.peso, historial_pesos.peso_datetime FROM historial_pesos
                 WHERE historial_pesos.pac_id = ?
                 ORDER BY historial_pesos.peso_datetime
                """
        return [item[1] for  item in self.cur.execute(sql,(pac_id,))]
        
        