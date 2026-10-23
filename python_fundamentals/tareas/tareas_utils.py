#!/usr/bin/env python3

def cargar(filename):
    try:

        lst = []

        with open(filename, "r") as file:
            for line in file:
                lst.append(line)

        nueva_tarea = input("Ingrese una nueva tarea: ")

        while nueva_tarea != "":
            lst.append(f"{nueva_tarea}\n")
            nueva_tarea = input("Ingrese una nueva tarea: ")
            
        return lst

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None

def guardar(lst, filename):
    with open(filename, "w") as file:
        for tarea in lst:
            file.write(tarea)
    

def mostrar(lst):
    if not lst:
        print("La lista está vacía")
    else:
        num = 1
        for elemento in lst:
            print(f"{num}. {elemento}")
            num += 1 

def eliminaar_tarea(lst):
    try:
        index = int(input("Ingrece el indice de la tarea a borrar: "))
        index -= 1

        del lst[index]

        return lst

    except IndexError:
        print("El indice ingresado no existe")