"""Consigna del Ejercicio:
1. Crear una matriz de calificaciones:
o Crear una matriz que represente las calificaciones de los estudiantes. La matriz 
debe tener filas representando a los estudiantes y columnas representando las 
materias.
o Inicializar la matriz con calificaciones aleatorias entre 1 y 10.
2. Mostrar la matriz:
o Implementar una función que imprima la matriz de calificaciones de forma 
legible.
3. Calcular el promedio de calificaciones:
o Implementar una función que calcule y muestre el promedio de calificaciones 
de cada estudiante.
o Implementar una función que calcule y muestre el promedio de calificaciones 
de cada materia.
"""


import random

def matriz(estudiantes,materias):
    estudiantes=["juan", "alberto", "martin", "federico", "tomas", "lucas"]
    materias=["Matematica", "Ingles", "Fisica", "Biologia", "Arte", "Musica", "Ed. Fisica"]
    return [[0]*estudiantes for fil in range(materias)]

def llenar_matriz(materias):
    estudiantes = len(materias)
    materias = len(materias*[0])
    for fil in range(estudiantes):
        for col in range(materias):
            num_aleatorio = random.randint(1,10)
            materias[fil][col] = num_aleatorio

