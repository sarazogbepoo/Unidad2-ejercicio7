# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:37:58 2020

@author: Sara Zogbe
"""

#Ejercicio Nº 7 (Sobrecarga por derecha)
#a- Defina una clase Hora que registre: hora, minutos y segundos, en el formato de 24 horas.
#b- Sobrecargue los métodos necesarios, para que pueda ejecutarse el Main que a continuación
#se propone.
from ClaseFechahora import FechaHora, bisiesto 

class Hora:
    __hora=0
    __minuto=0
    __segundo=0
    def __init__(self,hora=0,minuto=0,segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo= segundo
    
    def get_minuto(self):
        return self.__minuto
    def get_segundo(self):
        return self.__segundo
    def get_hora(self):
        return self.__hora   
    def Mostrar(self):
        s=' ' +repr(self.__hora)+':'+repr(self.__minuto)+':'+repr(self.__segundo) 
        print(s)
   
    
    
    def __radd__(self, otro):
        h=self.get_hora()+otro.get_hora()
        m=self.get_minuto()+otro.get_minuto()
        s=self.get_segundo()+otro.get_segundo()
        aux=FechaHora(otro.get_dia(),otro.get_mes(),otro.get_año(),h,m,s)
        print("Estoy en la clase Hora en el radd" )
        print("self", type(self))
        print("otro", type(otro))
        #aux.__hora+=h
        #aux.__minuto+=m
        #aux._segundo+=s
        return aux             
            
    def __add__(self, otro):
        print("Estoy en la clase Hora en el add" )
        print("self", type(self))
        print("otro", type(otro))
        input
        aux=self
        h=self.get_hora()+otro.get_hora()
        m=self.get_minuto()+otro.get_minuto()
        s=self.get_segundo()+otro.get_segundo()
        #if  h>=24:
        #    h=aux.__hora -24
        #    d=otro.get_dia()+1
        aux=FechaHora(otro.get_dia(),otro.get_mes(),otro.get_año(),h,m,s)
       
        #aux.__hora+=h
        #aux.__minuto+=m
        #aux._segundo+=s
        return aux                        
       # if  aux.__hora>=24:
       #     aux.__hora=aux.__hora -24
       #     aux.__dia=aux.__dia+1

if __name__ == '__main__':
    #d = int(input("Ingrese Dia: "))
    #mes = int(input("Ingrese Mes: "))
    #a = int(input("Ingrese Año: "))
    #h = int(input("Ingrese Hora: "))
    #m = int(input("Ingrese Minutos: "))
    #s = int(input("Ingrese Segundos: "))
    f = FechaHora(1,1,2020,1,20,10)
    f.Mostrar()
    input()
    #h1 = int(input("Ingrese Hora: "))
    #m1 = int(input("Ingrese Minutos: "))
    #s1 = int(input("Ingrese Segundos: "))
    r = Hora(24, 30,20)
    r.Mostrar()
    input()
    f1 = f +r 
    print("f1+r")
    f1.Mostrar()
    input()
    f1=r+f
    print("r+f1")
    f1.Mostrar()
    input()
    f3 = r + f 
    f3.Mostrar()
    input()
    f4 = f3-1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de 
                   # días indicada por el número entero
    f4.Mostrar()
    input()	

