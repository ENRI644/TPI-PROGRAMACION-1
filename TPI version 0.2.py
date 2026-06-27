# La empresa Play.In desea desarrollar una plataforma educativa destinada a estudiantes de
# nivel primario que permita aprender mediante actividades interactivas.
# Para ello solicita a los equipos de desarrollo la construcción de una aplicación que integre
# distintos juegos o herramientas didácticas dentro de un único sistema.
# El objetivo es que el usuario pueda elegir libremente qué actividad utilizar y regresar al menú
# principal tantas veces como desee.
# Cada integrante del equipo deberá ser responsable principal del desarrollo de al menos una
# actividad, aunque todo el grupo será responsable del funcionamiento integral del sistema.
# Ejemplo
# ****************************************************
# BIENVENIDOS A 4IN1
# ****************************************************
# 1- Ahorcado
# 2- Adivina la palabra
# 3- A Multiplicar
# 4- ¿Cuánto conoces los números?
# 0- Salir
# Ingresa tu opción:
# *****************************************************
# (si ingreso 4)
# ****************************************************
# 4-¿Cuánto conoces los números?
# ****************************************************
# ¿El número 3 es un número primo?
# 1- Si
# 2- No
# 3- Volver al menú sin contestar
# Ingresa tu opción:
# *****************************************************

def ingresoNum (): #FUNCION PARA ASEGURARME QUE SE INGRESA UN NUMERO.
    band = True
    while (band):
        try:
            num = int(input(print("Ingrese un numero")))
            band = False
        except(ValueError):
            print("ERROR AL INGRESAR EL DATO, DEBE SER NUMERO")
    return num

#DEFINICION E INICIALIZACION DE VARIABLES
opc = -1 #VARIABLE USADA PARA EL MENU PRINCIPAL

while (opc !=0): #MENU PRINCIPAL DE LOS JUEGOS, SE REPETIRA HASTA QUE EL USUARIO DECIDA SALIR INGRESANDO 0.
    print("¿Que juego desea probar?")
    print("1 - Juego A")
    print("2 - Juego B")
    print("3 - Juego C")
    print("4 - Juego D")
    print("5 - Juego E")
    print("6 - Juego F")
    print("0 - SALIR")
    opc=ingresoNum()
    if(opc > 6 or opc < 0):
        print("OPCION INVALIDA, INGRESE UN NUMERO ENTRE 0 Y 6")
    elif(opc == 4):
        print("LLAMO AL JUEGO 4")
    elif(opc == 6):
        print("LLAMO AL JUEGO 6")
    elif(opc == 0):
        print("Gracias vuelva pronto")
#prueba0 = int(input(print("Ingrese un numero")))
