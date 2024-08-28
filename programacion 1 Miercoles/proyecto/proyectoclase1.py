matriz_eventos=[]
columnas=2
filas=4

for fil in range(filas):
    matriz_eventos.append([])
    for col in range(columnas):
        matriz_eventos[fil].append(0)

for i in range(3):
    matriz_eventos[0][0]= ""
    matriz_eventos[1][0]= "a"
    matriz_eventos[2][0]= "b"
    matriz_eventos[3][0]= "c"
    matriz_eventos[0][1]= "Tipo de evento"
    matriz_eventos[1][1]= "Teatro Stand Up"
    matriz_eventos[2][1]= "Cine"
    matriz_eventos[3][1]= "Concierto"


# Imprimir la lista ordenada con formato de f-strings
for id, nombre in matriz_eventos:
    print(f"{id:>30} {nombre:<30} ")

cliente_selec_tip_evento=input("Ingrese la letra del tipo de evento que usted desea concurrir: ")


"""
if cliente_selec_tip_evento == "a" or cliente_selec_tip_evento == "A":

if cliente_selec_tip_evento == "b" or cliente_selec_tip_evento == "B":

if cliente_selec_tip_evento == "c" or cliente_selec_tip_evento == "C":
"""
