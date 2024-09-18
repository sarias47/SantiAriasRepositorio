import re

def validar(entrada):#valida que la entrada no sea simplemente numero
    if re.match(r"^-?\d+$",entrada):
        return 1
    else:
        return 0
    
def validar_email(email): 
    validacion_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Expresión regular para validar el formato del email
    if re.match(validacion_email, email):
        return 1
    else:
        return 0
    
def validar_dni(dni): 
    validacion_dni = r'^\d{7,8}$'  # Expresión regular para validar el formato del DNI
    if re.match(validacion_dni, dni):
        return 1
    else:
        return 0

def validar_contraseña(contraseña):# Expresion regular para validar contraseña
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,16}$",contraseña):
        return 1
    else:
        return 0
    
def validar_nombre(nombre):#Expresion regular para validar el nombre del ususario
    if re.match(r"^([a-zA-ZáéíóúÁÉÍÓÚñÑ]+)(\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$", nombre):
        return 1
    else:
        return 0

def validar_usuario(usuario):#Expresion regular para validar el usuario ingrsado
    if re.match(r"^[a-zA-Z][a-zA-Z0-9_]{2,15}$",usuario):
        return 1
    else:
        return 0