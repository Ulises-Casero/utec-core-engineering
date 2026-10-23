#!/usr/bin/env python3

import tareas_utils

lista = []

lista = tareas_utils.cargar("tareas.txt")

tareas_utils.mostrar(lista)

lista = tareas_utils.eliminaar_tarea(lista)

tareas_utils.mostrar(lista)

tareas_utils.guardar(lista, "tareas.txt")

print("="*15+"\n")
print("Nuevas tareas del archivo: ")
lista = tareas_utils.cargar("tareas.txt")
tareas_utils.mostrar(lista)