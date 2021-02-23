# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:25:22 2021

@author: Henao
"""
def funcion_a()->None:
    print("Usted a escogido la opción a del menú")
    
def funcion_b()->None:
    print("Usted a escogido la opción b del menú")
    
def funcion_c()->None:
    print("Usted a escogido la opción c del menú")
    
def funcion_d()->None:
    print("Usted a escogido la opción d del menú")
    
#PROGRAMA PRINCIPAL

print("MENÚ PRINCIPAL")
print(""""
      Opción a
      Opción b
      Opción c
      Opción d
      """)
      
x = input("Seleccione una opción: ")

if x == "a":
    funcion_a()
elif x == "b":
    funcion_b()
elif x == "c":
    funcion_c()
elif x == "d":
    funcion_d()
else:
    print("Selección invalida")