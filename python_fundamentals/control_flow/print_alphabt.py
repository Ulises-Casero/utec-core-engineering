#!/usr/bin/env python3

abc = "abcdefghijklmnopqrstuvwxyz"
solucion = ""

for value in range(len(abc)):
    if abc[value] != "e" and abc[value] != "q":
        solucion = solucion + abc[value]        
print(solucion)
