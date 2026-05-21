# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:14:29 2026

@author: gusta
"""
import math

#Exemplo classes

# class Celula:
#     pass

# #Literalmente fazendo objetos !!!!
# celula1 = Celula()
# celula2= Celula()

# celula1.nome = "Zé lelé"
# celula1.x = 0
# celula1.y= 0

# celula2.nome = "Jurandir"
# celula2.x = 8
# celula2.y= 7

class Celula:
    def __init__(self,nome, x, y):
        self.nome = nome
        self.x=x
        self.y=y
    
    def getNome(self):
        return self.nome
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def calculaDisctancia(celula1, celula2):
        distancia = math.sqrt((celula1.x - celula2.x) ** 2 +
                              (celula1.y - celula2.y) ** 2)
        
        return distancia

celula1 = Celula("Zé lelé", 1 , 2)
celula2 = Celula ("Maria lelé",4,2)
print(celula1.getNome())
print("Distancia:"+str(Celula.calculaDisctancia(celula1, celula2)))

