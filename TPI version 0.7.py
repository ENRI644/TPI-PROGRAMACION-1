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


import random #BIBLIOTECA DE PYTHON

def ingresoNum (): #FUNCION PARA ASEGURARME QUE SE INGRESA UN NUMERO.
    band = True
    while (band):
        try:
            num = int(input("Ingrese un numero "))
            band = False
        except(ValueError):
            print("ERROR AL INGRESAR EL DATO, DEBE SER NUMERO")
    return num

def LimpiarPantalla (): #FUNCION PARA "LIMPIAR" LA PANTALLA.
    print("\n" * 100)
    return

def controlMenus (mensaje,opc): #FUNCION PARA CONTROLAR LOS MENUS ENTRE EL JUEGO ELEJIDO Y EL MENU PRINCIPAL.
    jugar = -1
    while (jugar != 0) and (jugar != 1):
        print("REGLAS DEL JUEGO:")
        print(mensaje)
        while jugar != 0 and jugar != 1:
            print("¿Desea jugar (Ingrese 1) o volver al menu?(Ingrese 0)")
            jugar = ingresoNum()
            if(jugar == 0): #VUELVE AL MENU PRINCIPAL
                return
            elif(jugar == 1): #COMIENZA EL JUEGO
                LimpiarPantalla()
                if opc == 4:
                    Juego4()
                elif opc == 6:
                    print("LLAMO AL JUEGO 6 (EN DESARROLLO)")
                elif opc == 1:
                    juego1()
                elif opc == 2:
                    print("LLAMO AL JUEGO 2 (EN DESARROLLO)")   
                elif opc == 3:
                    print("LLAMO AL JUEGO 3 (EN DESARROLLO)")
                elif opc == 5:
                    print("LLAMO AL JUEGO 5 (EN DESARROLLO)")
            else:
                print("OPCION INVALIDA, INGRESE 1 PARA JUGAR O 0 PARA VOLVER AL MENU")
            jugar = -1

#ADIVINA EL NUMERO
#JUEGO DONDE EL USUARIO DEBE ADIINAR UN NUMERO GENERADO ALEATORIAMENTE POR LA COMPUTADORA
#EL PROGRAMA VA DANDO PISTAS HASTA QUE EL JUGADOR ACIERTA.

def guardar_puntaje(intentos): #SIRVE PARA GUARDAR EN UN ARCHIVO CUANTOS INTENTOS NECESITO
    archivo = open("puntajes.txt", "a") #PYHTON CREA EL ARCHIVO AUTOMATICAMENTE SI NO EXISTE
    archivo.write("Ganó en " + str(intentos) + " intentos\n")
    archivo.close() #SE CIERRA EL ARCHIVO.

def juego1():
    numero_secreto = random.randint(1, 20) #PARA GENERAR NUMEROS AL AZAR
    intentos = 0

    print("=== ADIVINA EL NÚMERO ===")
    print("Debes adivinar un número entre 1 y 20") #INSTRUCCIONES SENCILLAS

    historial=[] #CREA UNA LISTA VACIA 

    while True: #REPETIR HASTA ENCONTRAR EL NUMERO CORRECTO
        
        numero = ingresoNum() #PIDE EL NUMERO AL USUARIO
        historial.append(numero) #AGREGA A LA LISTA LOS INTENTOS DEL USUARIO
        intentos += 1

#COMPARA LAS RESPUESTAS Y DA LAS PISTAS
        if numero < numero_secreto:
            print("Más alto")

        elif numero > numero_secreto:
            print("Más bajo")

        else:
            print("¡Correcto!")
            print("Lo lograste en", intentos, "intentos")
            print("Tus intentos fueron: ", historial)
            guardar_puntaje(intentos) #GUARDA EL RESULTADO
            break


def Juego4 (): #AHORCADO
    print("AHORCADO")
    palabra = ""
    vidas = 6
    letrasErradas = []
    palabra = input("ingrese la palabra a adivinar: ")
    palabraVec = PalabraVector(palabra) #PASO LA PALÑABRA A UN VECTOR
    adivina = PalabraOculta(palabraVec) #USO UN VECTOR AUXILIAR PARA MOSTRAR LOS GUIONES
    aciertos = 0
    while (vidas > 0) and (aciertos < len(adivina)) : #CICLO DEL JUEGO.
        LimpiarPantalla()
        band = True
        print(adivina)
        print(f"Ingrese una letra: (vidas: {vidas}, letras erradas: {letrasErradas})")
        letra = input("")
        for i in range(len(palabraVec)):
            if ((letra == palabraVec[i]) and (letra != adivina[i])):
                adivina[i] = letra
                band = False #SI SE ENCONTRO LA LETRA CAMBIO LA BANDERA
                aciertos += 1
        if band: #SI NO SE CAMBIO LA BANDERA, NO ACERTO LETRA, RESTO VIDA.
            vidas -= 1
            letrasErradas.append(letra)
        if (aciertos == len(adivina)):
            print("GNASTE, ADIVINASTE LA PALABRA")
        else:
            print("PERDISTE, te quedaste sion vidas. La palabra era: ", palabra)
    return

# def Juego6 (): #VEINTIUNO
#     jugadores = 0
#     while (jugadores < 1 or jugadores > 4): #CONTORLO QUE LOS JUGADORES SEAN CORRECTOS
#         print("VEINTIUNO")
#         print("Cuantos jugadores son (min 1 max 4)?")
#         jugadores = ingresoNum()
#         if (jugadores < 1 or jugadores > 4):
#             print("OPCION INVALIDA, INGRESE UN NUMERO ENTRE 1 Y 4")
#     #HACER EL CODIGO DEL JUEGO
#     return

def Juego2 (): #JUEGO B
    print("JUEGO B")
    #HACER EL CODIGO DEL JUEGO B QUIEN CORRESPONDA
    return
def Juego3 (): #JUEGO C
    print("JUEGO C")
    #HACER EL CODIGO DEL JUEGO C QUIEN CORRESPONDA
    return
def Juego5 (): #JUEGO E
    print("JUEGO E")
    #HACER EL CODIGO DEL JUEGO E QUIEN CORRESPONDA
    return

def PalabraVector (palabra): #FUNCION PARA TRANSFORMAR UNA PALABRA EN UN VECTOR DE LETRAS.
    vector = [0] * len(palabra)
    for i in range(len(palabra)):
        vector[i] = palabra[i]
    return vector 

def PalabraOculta(vector):
    vecAux= [0] * len(vector)
    for i in range(len(vector)):
        vecAux[i] = "_"
    return vecAux


#DEFINICION E INICIALIZACION DE VARIABLES
opc = -1 #VARIABLE USADA PARA EL MENU PRINCIPAL
#PROCESOS (MENU PRINCIPAL)
while (opc !=0): #MENU PRINCIPAL DE LOS JUEGOS, SE REPETIRA HASTA QUE EL USUARIO DECIDA SALIR INGRESANDO 0.
    print("¿Que juego desea probar?")
    print("1 - ADIVINA EL NUMERO (1 JUGADOR)") #DANI
    print("2 - Juego B")
    print("3 - Juego C")
    print("4 - AHORCADO (2 JUGADORES)") #ENRI estuvo aqui
    print("5 - Juego E")
    print("6 - Juego F")
    print("0 - SALIR")
    opc=ingresoNum()
    LimpiarPantalla()
    if(opc > 6 or opc < 0):
        print("OPCION INVALIDA, INGRESE UN NUMERO ENTRE 0 Y 6")
    elif(opc == 1):
        reglas = "=== ADIVINA EL NÚMERO === \n Debes adivinar un número entre 1 y 20"
    elif(opc == 2):
        reglas = "Reglas del juego B(EN DESARROLLO)"
    elif(opc == 3):
        reglas = "Reglas del juego C (EN DESARROLLO)"
    elif(opc == 4):
        reglas = "2 jugadores, el primero ingresa una palabra y el segundo debe adivinarla letra por letra, tiene 6 vidas"
    elif(opc == 5):
        reglas = "Reglas del juego E (EN DESARROLLO)"
    elif(opc == 6):
        reglas = "Reglas del juego F (EN DESARROLLO)"
    elif(opc == 0):
        print("Gracias vuelva pronto")
    if(opc < 7 and opc > 0):
        controlMenus(reglas,opc) #LLAMO A LA FUNCION Y LE PASO LAS REGLAS Y EL NUMERO DEL JUEGO QUE SE ELIJIO
