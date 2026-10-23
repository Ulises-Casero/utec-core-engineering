#!/usr/bin/env python3
import random

lst=[]

nombre = input("Ingresar nombre: ")


while nombre != "":
    lst.append(nombre)
    nombre = input("Ingresar nombre: ")

if not lst:
    print("no se ingresaron nombres")
else:
    print("Nombre seleccionado: "+random.choice(lst))
    