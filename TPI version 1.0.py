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
                    Juego6()
                elif opc == 1:
                    juego1()
                elif opc == 2:
                    Juego2()   
                elif opc == 3:
                    Juego3()
                elif opc == 5:
                    Juego5()
            else:
                print("OPCION INVALIDA, INGRESE 1 PARA JUGAR O 0 PARA VOLVER AL MENU")
            jugar = -1

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
            LimpiarPantalla()
            print("¡Correcto!")
            print("Lo lograste en", intentos, "intentos")
            print("Tus intentos fueron: ", historial)
            break
    return

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
            print("GNASTE, ADIVINASTE LA PALABRA, ", palabra)
        else:
            print("PERDISTE, te quedaste sion vidas. La palabra era: ", palabra)
    return

def Juego2 ():
    print("¡Bienvenido a la Búsqueda del tesoro!")
    print("1- Nivel normal")
    print("2- Nivel difícil")
    print("3- Créditos")
    print("4- Salida")

    opcion = input("¡Elija una opción!: ")

    # MENÚ
    if opcion == "1":
        tamaño = 3
    elif opcion == "2":
        tamaño = 5
    elif opcion == "3":
        print("Créditos... Hecho por Sol 🌞")
        return()
    elif opcion == "4":
        return()
    else:
        print("Opción inválida")
        return()

    # TESORO (se genera UNA sola vez)
    tesoro_x = random.randint(1, tamaño)
    tesoro_y = random.randint(1, tamaño)

    # JUEGO
    while True:
        x = int(input(f"Ingrese fila (1 a {tamaño}): "))
        y = int(input(f"Ingrese columna (1 a {tamaño}): "))

        # validar rango
        if not (1 <= x <= tamaño and 1 <= y <= tamaño):
            print("❌ Fuera de rango")
            continue

        # comparar con el tesoro
        if x == tesoro_x and y == tesoro_y:
            LimpiarPantalla()
            print("¡Encontraste el tesoro!")
            break
        else:
            print("Ups! ahí no estaba, segui intentando 👉")

def Juego3 (): 
    print("PIEDRA PAPEL O TIJERA - AL MEJOR DE 3")

    victoriasJugador = 0
    victoriasComputadora = 0

    opciones = ["piedra", "papel", "tijera"]

    while victoriasJugador < 2 and victoriasComputadora < 2:
        LimpiarPantalla()
        print("---------------------")
        print("Jugador:", victoriasJugador)
        print("Computadora:", victoriasComputadora)

        jugador = input("Elija piedra, papel o tijera: ").lower()

        while jugador not in opciones:
            print("OPCION INVALIDA")
            jugador = input("Elija piedra, papel o tijera: ").lower()

        computadora = random.choice(opciones)

        print("La computadora eligio:", computadora)

        if jugador == computadora:
            print("EMPATE")

        elif ((jugador == "piedra" and computadora == "tijera") or
              (jugador == "papel" and computadora == "piedra") or
              (jugador == "tijera" and computadora == "papel")):
            print("GANASTE LA RONDA")
            victoriasJugador += 1

        else:
            print("PERDISTE LA RONDA")
            victoriasComputadora += 1

    print("---------------------")

    if victoriasJugador == 2:
        print("¡¡GANASTE LA PARTIDA!!")
    else:
        print("LA COMPUTADORA GANO LA PARTIDA")

    return

def Juego5 (): #JUEGO E
    # Variables para guardar los puntos.
    puntos_jugador = 0
    puntos_maquina = 0

    print("===== BATALLA DE DADOS =====")

    # El ciclo se repite 5 veces (5 rondas).
    for ronda in range(1, 6):

        print("\nRonda", ronda)

        # Espera a que el jugador presione Enter.
        input("Presiona Enter para lanzar el dado...")

        # Cada participante lanza su dado.
        dado_jugador = lanzar_dado()
        dado_maquina = lanzar_dado()

        # Se muestran los resultados.
        print("Tu dado fue:", dado_jugador)
        print("La computadora sacó:", dado_maquina)

        # Se comparan los valores para saber quién ganó.
        if dado_jugador > dado_maquina:
            print("¡Ganaste esta ronda!")
            puntos_jugador += 1

        elif dado_maquina > dado_jugador:
            print("La computadora ganó esta ronda.")
            puntos_maquina += 1

        else:
            print("Empate. Nadie suma puntos.")

    # Se muestran los puntos finales.
    print("\n===== RESULTADO FINAL =====")
    print("Puntos del jugador:", puntos_jugador)
    print("Puntos de la computadora:", puntos_maquina)

    # Se determina el ganador de la partida.
    if puntos_jugador > puntos_maquina:
        print("¡Felicidades! Ganaste la partida.")

    elif puntos_maquina > puntos_jugador:
        print("La computadora ganó la partida.")

    else:
        print("La partida terminó en empate.")
    return

def Juego6():

    LimpiarPantalla()

    print("DESAFIO MATEMATICO")
    print("resuelve corectamente las 5 operaciones y gana puntos") #INSTRUCCIONES

    nombre = input("Ingrese su nombre: ")#PIDO EL NOMBRE AL JUGADOR Y LO GUARDO EN LA VARIABLE NOMBRE 

    puntos = 0 #INICIALIZO UNA VARIABLE DE PUNTOS EN 0 PARA CONTARLOS 

    operaciones = ["+","-","*"] #GUARDO LAS OPERACIONES QUE VOY A UTILIZAR 

    for i in range(5):

        LimpiarPantalla()

        print("DESAFIO MATEMATICO")
        print("Jugador: ",nombre)
        print("Puntaje: ",puntos)
        print("-------------------------")
        print("Pregunta",i+1)

        num1 = random.randint(1,10) #PARA QUE ELIJA NUMEROS AL AZAR PARA LAS OPERACIONES  
        num2 = random.randint(1,10)

        operacion = random.choice(operaciones)#PARA QUE ELIJA UNA OPERACION AL AZAR 
        #SUMA  
        if operacion == "+":
            resultado = num1 + num2

        # RESTA
        elif operacion == "-":

        # EVITA RESULTADOS NEGATIVOS
            if num2 > num1:
                aux = num1
                num1 = num2
                num2 = aux

            resultado = num1 - num2
        # MULTIPLICACION
        else:
            resultado = num1 * num2    
       
        #MUESTRO LA OPERACION PARA EL JUGADOR 
        print()
        print(num1,operacion,num2)
        #PIDO EL RESULTADO
        respuesta = ingresoNum()
        #SI LA RESPUESTA ES CORRECTA SUMA UN PUNTO
        if respuesta == resultado:

            print("¡RESPUESTA CORRECTA!")
            puntos += 1
        #SI NO LO ES MUESTRO EL RESULTADO  
        else:

            print("RESPUESTA INCORRECTA.")
            print("La respuesta correcta era: ",resultado)

        input("Presione ENTER para continuar...")

    LimpiarPantalla()
    #MUESTRO EL RESULTADO CON EL NOMBRE DEL JUGADOR
    print("RESULTADO FINAL")
    print("Jugador:",nombre)
    print("Puntaje obtenido: ",puntos,"/5")

    if puntos == 5:
        print("¡¡EXCELENTE!!")

    elif puntos >= 3:
        print("¡MUY BIEN!")

    else:
        print("SEGUI PRACTICANDO.")

    print()

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

# Función que simula el lanzamiento de un dado.
# random.randint(1,6) devuelve un número aleatorio entre 1 y 6.
def lanzar_dado():
    return random.randint(1, 6)


#DEFINICION E INICIALIZACION DE VARIABLES
opc = -1 #VARIABLE USADA PARA EL MENU PRINCIPAL
#PROCESOS (MENU PRINCIPAL)
while (opc !=0): #MENU PRINCIPAL DE LOS JUEGOS, SE REPETIRA HASTA QUE EL USUARIO DECIDA SALIR INGRESANDO 0.
    print("¿Que juego desea probar?")
    print("1 - ADIVINA EL NUMERO (1 JUGADOR)") #DANI
    print("2 - ENCONTRAR EL TESORO (1 JUGADOR)") #SOL 🌞
    print("3 - PIEDRA PAPEL O TIJERA (1 JUGADOR)") #IGNI
    print("4 - AHORCADO (2 JUGADORES)") #ENRI estuvo aqui
    print("5 - BATALLA DE DADOS (1 JUGADOR)") #Manu
    print("6 - DESAFIO MATEMATICO (1 JUGADOR)") #Juli
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
        reglas = "Piedra, Papel o Tijera al mejor de 3 rondas. Gana quien consiga mas victorias."
    elif(opc == 4):
        reglas = "2 jugadores, el primero ingresa una palabra y el segundo debe adivinarla letra por letra, tiene 6 vidas"
    elif(opc == 5):
        reglas = "1. Se juegan 5 rondas. \n 2. En cada ronda el jugador y la computadora lanzan un dado. \n 3. El número más alto gana la ronda. \n 4. Si ambos sacan el mismo número, hay empate. \n 5. Al finalizar las 5 rondas, gana quien tenga más puntos."
    elif(opc == 6):
        reglas = "resuelve corectamente las 5 operaciones y gana puntos"
    elif(opc == 0):
        print("Gracias vuelva pronto")
    if(opc < 7 and opc > 0):
        controlMenus(reglas,opc) #LLAMO A LA FUNCION Y LE PASO LAS REGLAS Y EL NUMERO DEL JUEGO QUE SE ELIJIO
