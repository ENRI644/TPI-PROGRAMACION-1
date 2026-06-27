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
            num = int(input("Ingrese un numero "))
            band = False
        except(ValueError):
            print("ERROR AL INGRESAR EL DATO, DEBE SER NUMERO")
    return num

def LimpiarPantalla (): #FUNCION PARA "LIMPIAR" LA PANTALLA.
    print("\n" * 100)
    return

def Juego4 (): #AHORCADO
    jugar = -1
    print("Ahorcado")
    print("REGLAS: ")
    print("2 jugadores, el primero ingresa una palabra y el segundo debe adivinarla letra por letra, tiene 6 vidas")
    while jugar != 0 and jugar != 1:
        print("¿Desea jugar (Ingrese 1) o volver al menu?(Ingrese 0)")
        jugar = ingresoNum()
        if(jugar == 0): #VUELVE AL MENU PRINCIPAL
            return
        elif(jugar == 1): #COMIENZA EL JUEGO
            palabra = ""
            vidas = 6
            letrasErradas = []
            palabra = input("ingrese la palabra a adivinar: ")
            #HACER ELCODIGO DEL JUEGO.
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

            #print("FUNCIONO")
            jugar = -1 #RESETEO LA VARIABLE PARA QUE SE VUELVA A PREGUNTAR AL TERMINAR EL JUEGO
        else:
            print("OPCION INVALIDA, INGRESE 1 PARA JUGAR O 0 PARA VOLVER AL MENU")

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
while (opc !=0): #MENU PRINCIPAL DE LOS JUEGOS, SE REPETIRA HASTA QUE EL USUARIO DECIDA SALIR INGRESANDO 0.
    print("¿Que juego desea probar?")
    print("1 - Juego A")
    print("2 - Juego B")
    print("3 - Juego C")
    print("4 - AHORCADO (2 JUGADORES)")
    print("5 - Juego E")
    print("6 - Veintiuno")
    print("0 - SALIR")
    opc=ingresoNum()
    LimpiarPantalla()
    if(opc > 6 or opc < 0):
        print("OPCION INVALIDA, INGRESE UN NUMERO ENTRE 0 Y 6")
    elif(opc == 4):
        #print("LLAMO AL JUEGO 4")
        Juego4()
    elif(opc == 6):
        print("LLAMO AL JUEGO 6")
    elif(opc == 0):
        print("Gracias vuelva pronto")
#prueba0 = int(input(print("Ingrese un numero")))
