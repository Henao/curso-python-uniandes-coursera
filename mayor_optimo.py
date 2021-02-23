# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:59:51 2021

@author: Henao
"""
def mayor_optimo(a: int, b: int, c: int, d: int)->int:
    mayor = a
    if (b > mayor):
        mayor = b;
    if (c > mayor):
            mayor = c;
    if (d > mayor):
            mayor = d;
    return mayor
        