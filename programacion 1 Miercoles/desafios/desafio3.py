matriz_peliculas=[
    [1000, "Piratas del caribe", 1.45, "Netflix", "No apt"],
    [1001, "Transformers", 2.24, "Prime video", "No apt"],
    [1002, "Barbie", 2.16, "Hbo", "apt"],
    [1003, "High school musical", 2.37, "Disney plus", "apt"],
    ]

#Recorto los nombres de las peliculas
nombre_peli_recort=[[id, nombre[:12], duracion, plataforma, edad_permitida] for id, nombre, duracion, plataforma, edad_permitida in matriz_peliculas]

#Ordeno por duracion
pelis_orednadas = sorted(nombre_peli_recort, key=lambda x: (-x[2], x[1]))

# Imprimir la lista ordenada con formato de f-strings
print(f"{'ID':>4} {'Nombre':<12} {'duracion':>10} {'plataforma':>5} {'edad_permitida':>10}")
print('-' * 55)
for id, nombre, duracion, plataforma, edad_permitida in pelis_orednadas:
    print(f"{id:>4} {nombre:<12} {duracion:>10} {plataforma:>10} {edad_permitida:>10}")