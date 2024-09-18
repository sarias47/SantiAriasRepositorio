import re

matriz_peliculas=[
    [1000, "Piratas del caribe", 1.45, "Netflix", "No apt"],
    [1001, "Transformers", 2.24, "Prime video", "No apt"],
    [1002, "Barbie", 2.16, "Hbo", "apt"],
    [1003, "High school musical", 2.37, "Disney plus", "apt"],
    ]


usuarios=[["santino", "sarias2024@gmail.com", "sarias2024", "asdasd", 45518260]]

#Recorto los nombres de las peliculas
nombre_peli_recort=[[id, nombre[:12], duracion, plataforma, edad_permitida] for id, nombre, duracion, plataforma, edad_permitida in matriz_peliculas]

#Ordeno por duracion
pelis_orednadas = sorted(nombre_peli_recort, key=lambda x: (-x[2], x[1]))

def validar_nombre(nombre):
    if re.match(r"^([a-zA-ZáéíóúÁÉÍÓÚñÑ]+)(\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$", nombre):
        return 1
    else:
        return 0
    
def validar_email(email): 
    validacion_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Expresión regular para validar el formato del email
    if re.match(validacion_email, email):
        return 1
    else:
        return 0

def validar_contraseña(contraseña):
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,16}$",contraseña):
        return 1
    else:
        return 0

# Imprimir la lista ordenada con formato de f-strings
def inicio():
    print(f"{'ID':>4} {'Nombre':<12} {'duracion':>10} {'plataforma':>5} {'edad_permitida':>10}")
    print('-' * 55)
    for id, nombre, duracion, plataforma, edad_permitida in pelis_orednadas:
        print(f"{id:>4} {nombre:<12} {duracion:>10} {plataforma:>10} {edad_permitida:>10}")


def login():
    band=0
    while band==0:
        nombre=input("Ingrese su nombre completo: ")
        if validar_nombre(nombre) == 1:
            print("Nombre válido")
            bandera = 1
        else:
            print("Nombre invalido, porfavor ingreselo nuevamente")
        email = input("Ingrese su email: ")
        if validar_email(email) == 1:
            print("Correo valido")
            bandera=1
        else:
            print("Correo invalido. Ingreselo nuevamente.")
        contraseña = input("Ingrese su contraseña: ")
        if validar_contraseña(contraseña)==1:
            print("Contraseña valida")
            bandera=1
            inicio()
        else:
            print("Contraseña invalida, ingresela nuevamente")

login()
