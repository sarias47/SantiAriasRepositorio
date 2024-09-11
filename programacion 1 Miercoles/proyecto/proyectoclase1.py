from random import randint
import re
lista_id=[]
lista_tipo=['musica','familia','teatro','deporte']
eventos=[{
        "id":1001,
        "tipo":"musica",
        "nombre":"Milo J",
        "ubicacion":"Estadio de Morón",
        "fecha y hora":"25 de octubre, 21hs",
        "entradas": [
        {"seccion":"Platea","precio":30000,"disponibles":2000},
        {"seccion":"Campo delantero","precio":50000,"disponibles":3000},
        {"seccion":"Campo trasero","precio":40000,"disponibles":5000}
        ]
    },
    {
        "id":1002,
        "tipo":"familia",
        "nombre":"Plim Plim",
        "ubicacion":"Quality espacio",
        "fecha y hora":"5 de octubre, 17.30hs",
    }
    ]
 
def comprar(elegir1):
    if elegir1:
        for key in eventos:
            print(f"\nSelecciona entradas para {eventos[1]['nombre']}")
            for idx, entrada in enumerate(eventos[key]['entradas']):
                print(f"{idx+1}. {entrada['seccion']} - ${entrada['precio']} (Disponibles: {entrada['disponibles']})")
        
        opcion = int(input("Elige la sección (número): ")) - 1
        cantidad = int(input("¿Cuántas entradas deseas?: "))

        if 0 <= opcion < len(eventos['entradas']):
            seleccion = eventos['entradas'][opcion]
            if cantidad <= seleccion['disponibles']:
                print(f"Has seleccionado {cantidad} entradas en {seleccion['seccion']} a ${seleccion['precio']} cada una.")
                seleccion['disponibles'] -= cantidad  # Descontamos del inventario
            else:
                print("No hay suficientes entradas disponibles.")
        else:
            print("Opción no válida.")
    else:
        print("Evento no encontrado.")



def inicio():
    print("Tipos de eventos: ")
    print("-"*100)
    print('1)Música')
    print('2)Familia')
    print('3)Teatro')
    print('4)Deporte')
    print("-"*100)
    elegir=int(input("Seleccione una opción: "))
    eventos_funcion(elegir)


def interfaz():
    elegir1=0
    band=0
    while band==0:
        print('-' * 100)
        print('0)Inicio'.center(10,' '),'-1)Salir'.center(10,' '))
        print('-' * 100)
        elegir1=int(input("Seleccione una opción: "))
        if eventos.get("id") == :
            band=1
            comprar(elegir1)
        if elegir1 == 0:
            band=1
            inicio()
        if elegir1 == -1:
            band=1
            print("Fin") 


"""def Crear_matriz():
    i=0
    tipo=0

    while tipo != "E":
        print('a)Música'.center(10,' '),'b)Familia'.center(10,' '),'c)Teatro'.center(10,' '),'d)Cine'.center(10,' '),'e)Salir'.center(10,' '))
        tipo=input("Ingrese el tipo de evento: ")
        tipo=tipo.upper()
        if tipo != "E":    
            matriz_eventos.append([])
            nombre=input("Ingrese el nombre del evento: ")
            nombre=nombre.upper()
            capacidad=int(input("Ingrese su capacidad total: "))
            ubicacion=input("Ingrese la ubicacion del evento: ")
            ubicacion=ubicacion.upper()
            fecha=int(input("Ingrese la fecha del evento: "))
            hora=int(input("Ingrese la hora del evento: "))
            matriz_eventos[i].extend([tipo,nombre,capacidad,ubicacion,fecha,hora])
            i=i+1"""

def eventos_funcion(elegir):
    print("\nEventos Disponibles:")
    print(f"{'ID':<5} {'Nombre':<25} {'Tipo':<15} {'Ubicacion':<20}{'Fecha y hora':<10}")
    print("-" * 100)
    
    for evento in eventos:
        if evento["tipo"]==lista_tipo[elegir-1]:
            print(f"{evento['id']:<5} {evento['nombre']:<25} {evento['tipo']:<15} {evento['ubicacion']:<20}{evento['fecha y hora']:<10}")

    interfaz()





inicio()