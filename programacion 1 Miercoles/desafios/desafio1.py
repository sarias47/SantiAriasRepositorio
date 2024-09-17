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

estudiantes=5
materias=5
matriz5x5=[]
for fil in range(estudiantes):
    matriz5x5.append([])
    for col in range(materias):
        matriz5x5[fil].append(random.randint(1,10))

for i in range(5):
    matriz5x5[i][0]= "Estudiantes"

matriz5x5[0][0]="       "
matriz5x5[0][1]="Lengua"
matriz5x5[0][2]="Fisica"
matriz5x5[0][3]="Biologia"
matriz5x5[0][4]="Matematica"

def promedio():
    for i in range(5):
        print(matriz5x5[i])

    for i in range(4):
        num=matriz5x5[i+1][1]+matriz5x5[i+1][2]+matriz5x5[i+1][3]+matriz5x5[i+1][4]
        print("El promedio de los estudiantes es es: ", num/4)

    for i in range(4):
        prom=matriz5x5[1][i+1]+matriz5x5[2][i+1]+matriz5x5[3][i+1]+matriz5x5[4][i+1]
        print("El promedio de las materias es: ", prom/4)
promedio()