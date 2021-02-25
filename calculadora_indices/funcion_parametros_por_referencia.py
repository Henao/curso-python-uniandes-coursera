# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:24:39 2021

@author: Henao
"""
def funcion_con_parametro_de_tipo_dict(a: dict)->None:
    print("\nBienvenid@ a la función que recibe un parámetro de tipo dict")
    print("El valor del diccionario es :", a)
    a["valor"] += 1
    print("Ahora el diccionario es: ", a)
    

var = int(input("Digite un número entero: "))
print("\nVoy a crear un diccionario con ese número como valor")
dicc = {"valor":var}
print("\nEl diccionario antes de llamar a la funcion es: ", dicc)
funcion_con_parametro_de_tipo_dict(dicc)
print("\nEl diccionario despues de llamar a la función es: ", dicc)
