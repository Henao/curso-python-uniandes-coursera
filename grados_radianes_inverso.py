# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 07:37:21 2021

@author: Henao
"""


def fahrenheit_a_centigrados(grados_fahrenheit: float)->float:
    grados_celsius = float((grados_fahrenheit - 32) * (5/9))
    return grados_celsius

def centigrados_a_fahrenheit(grados_celsius: float)->float:
    grados_fahrenheit = float((grados_celsius * (9/5)) + 32)
    return grados_fahrenheit

def radianes_a_grados(radianes: float)->float:
    pi = 3.14159
    grados = (radianes*360) / (pi*2)
    return grados

def grados_a_radianes(grados: float)->float:
    pi = 3.14159
    radianes = (grados*pi*2)/360
    return radianes


def invertir_numero(numero: int)->int:
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    millares = numero % 10
    numero_invertido = int((unidades*1000) + (decenas*100) + (centenas*10) + millares)
    return numero_invertido