import json
import os
from time import sleep
from copy import deepcopy

# Constante rango si es cero cuando se llega al borde superior
def imprimir_ventana( ):

    altura_dialogo = 15
    altura_interaccion = 8  # Altura del área de interacción

    linea_actual = deepcopy(altura_dialogo)

    # Imprimir la línea superior de la ventana
    print("-" * (82))
    
    # Imprimir la sección de diálogo de la ventana
    for _ in range(altura_dialogo):
        print("|" + " " * 80 + "|")
    
    # Imprimir la línea divisoria entre la sección de diálogo y la de interacción
    print("-" * (82))
    
    # Imprimir la sección de interacción de la ventana
    for _ in range(altura_interaccion):
        print("|" + " " * 80 + "|")
    
    # Imprimir la línea inferior de la ventana
    print("-" * (82))

    return linea_actual

def obtener_mensajes_arcos(linea_actual):
    paquete_mensajes = []
    # Se abre el archivo "historia.json" en modo lectura con codificación utf-8
    with open("historia_prueba.json", "r", encoding="utf-8") as archivo:
        # Se lee el contenido del archivo
        contenido = archivo.read()

    # Se carga el contenido JSON en un diccionario de datos
    datos_lectura = json.loads(contenido)

    contador_arcos = 0
    nombres_arcos = list(datos_lectura.keys())
    lista_avance = []
    arco_actual = nombres_arcos[contador_arcos]

    while contador_arcos < len(nombres_arcos):
    # for nombre_arco, contenido_arco in datos_lectura.items():

        imprimir_nombre_arco(arco_actual)
        lista_avance.append(arco_actual)

        contenido_mensajes = datos_lectura[arco_actual].get("mensajes")

        cantidad_seccion = 0

        paquete_mensajes = []

        for mensaje in contenido_mensajes:
            paquete_mensajes.append(mensaje)

        pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion)

        contador_arcos += 1

        bandera_arco = True

        (bandera_arco, 
         contador_arcos, nombres_arcos) = terminar_juego(bandera_arco, contador_arcos, 
                                                         nombres_arcos)

        while bandera_arco == True:
            (arco_actual, lista_avance, 
             contador_arcos, bandera_arco) = restaurar_arco(contador_arcos, lista_avance, 
                                                            arco_actual, nombres_arcos, 
                                                            bandera_arco)
            
    linea = 22
    posicionar_linea(linea)
    for _ in range(2):
        print("|"+" " * 80)

    linea = 1
    posicionar_linea(linea)                                                      
    mensaje_final = ("| Gracias por jugar. ¡Hasta la próxima!\n\n"
                     "| Créditos:\n| Programado y escrito por:"
                     " Juan José Tobar y Jospeh Lievano")

    for caracter in mensaje_final:
        print(caracter, end="", flush=True)
        sleep(0.03)

    linea = 26
    posicionar_linea(linea)  

    return None

def terminar_juego(bandera_arco, contador_arcos, nombres_arcos):
    LINE_UP = '\033[1A'
    marcador = True

    while bandera_arco == True and marcador == True:

        linea = 22
        posicionar_linea(linea)
        for _ in range(2):
            print("|"+" " * 80)
        for _ in range(2):
            print(LINE_UP, end="")

        respuesta = input("| ¿Quiere cerrar el juego? (si ; no):")

        if respuesta.lower().replace(" ", "") == "si":
            bandera_arco = False
            marcador = False
            contador_arcos = len(nombres_arcos)

        elif respuesta.lower().replace(" ", "") == "no":

            bandera_arco = True
            marcador = False

        else: 
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|"+ " " * 80)

            for _ in range(2):
                print(LINE_UP, end="")

            msg_no_valido = "| Seleccione una opcion válida"
            for caracter in msg_no_valido:
                print(caracter, end="", flush=True)
                sleep(0.02)

            input("\n| Presione enter para continuar:")
    
    return bandera_arco, contador_arcos, nombres_arcos

def restaurar_arco(contador_arcos, lista_avance, arco_actual, nombres_arcos, bandera_arco):
    
    LINE_UP = '\033[1A'

    linea = 22
    posicionar_linea(linea)
    for _ in range(2):
        print("|"+" " * 80)
    for _ in range(2):
        print(LINE_UP, end="")

    respuesta = input("| ¿Quiere regresar a un arco? (si ; no):")

    if respuesta.lower().replace(" ", "") == "si":
        punto_retroceso = input("| ¿A cuál arco quiere regresar?:")

        if punto_retroceso.lower().replace(" ", "") in lista_avance:

            arco_actual = punto_retroceso.lower().replace(" ", "")

            contador_arcos = lista_avance.index(punto_retroceso.lower().replace(" ", ""))

            linea = 22
            posicionar_linea(linea)
            print("|"+" " * 80)
            print("|"+" " * 80)

            bandera_arco = False

        else:
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|"+ " " * 80)
            for _ in range(2):
                print(LINE_UP, end="")

            msg_no_hallado = "| La solicitud no se encuentra disponible"

            for caracter in msg_no_hallado:
                print(caracter, end="", flush=True)
                sleep(0.02)

            input("\n| Presione enter para continuar:")

    elif (respuesta.lower().replace(" ", "") == "no" 
          and contador_arcos < len(nombres_arcos)):
        
        arco_actual = nombres_arcos[contador_arcos]
        
        linea = 22
        posicionar_linea(linea)
        print("|"+" " * 80) 

        bandera_arco = False
    
    elif contador_arcos == len(nombres_arcos):

        bandera_arco = False

    else: 
        None

    return arco_actual, lista_avance, contador_arcos, bandera_arco

def imprimir_nombre_arco(nombre_arco):
    linea = 1
    posicionar_linea(linea)

    nombre_arco = nombre_arco[:-1].capitalize() + " " + nombre_arco[-1::]
    print("| ", end = "")

    for caracter in nombre_arco:
        print(caracter, end="", flush=True)
        sleep(0.1)

    linea = 23
    posicionar_linea(linea)
    input("| Presione enter para continuar:")

def pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion):
    
    lista_secciones = []

    constante_linea =  1
    constante_rango = 1

    for paquete in paquete_mensajes:

        orientacion_paquete = []

        mensaje_actual = (paquete.get("texto"))

        orientacion_paquete.append(paquete.get("orientacion"))
        orientacion_paquete.append(mensaje_actual)

        lista_secciones.append(orientacion_paquete)

        (linea_actual, cantidad_seccion, 
         constante_linea, constante_rango, lista_secciones) = imprimir_mensaje(linea_actual, 
                                                              cantidad_seccion, lista_secciones, 
                                                              constante_linea, constante_rango)
        
        linea = 23
        posicionar_linea(linea)

        input("| Presione enter para continuar:")

        if paquete.get("imagen"):
            archivo_imagen = paquete.get("imagen")
            borrar_pantalla( )
            imprimir_imagen(archivo_imagen )

        if paquete.get("alternativas"):
            alternativas = paquete.get("alternativas")

            (linea_actual, cantidad_seccion, 
            constante_linea, constante_rango,  lista_secciones) = recorrer_alternativas(alternativas, linea_actual, 
                                                                                       cantidad_seccion, constante_linea, constante_rango, lista_secciones)


    borrar_pantalla( )

def recorrer_alternativas(alternativas, linea_actual, cantidad_seccion, 
                         constante_linea, constante_rango, lista_secciones):

    LINE_UP = '\033[1A'

    #Posiciona la opción presione para continuar donde debe de ser
    linea = 17
    posicionar_linea(linea)

    while len(alternativas) != 0:

        opcion, alternativas = imprimir_alternativas(alternativas)

        if opcion in alternativas:

            lista_auxiliar = []
            lista_auxiliar.append(False)
            lista_auxiliar.append(alternativas[opcion][1])

            lista_secciones.append(lista_auxiliar)

            (linea_actual, cantidad_seccion, 
            constante_linea, constante_rango,  lista_secciones) = imprimir_mensaje(linea_actual, 
                                                                cantidad_seccion, lista_secciones, 
                                                                constante_linea, constante_rango)
            
            del alternativas[opcion]

            linea = 17
            posicionar_linea(linea)

            for _ in range(4):
                print("|"+" " * 80)

            for _ in range(4):
                print(LINE_UP, end="")

        else: 
            
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|"+ " " * 80)

            for _ in range(2):
                print(LINE_UP, end="")

            msg_no_valido = "| Seleccione una opcion válida"
            for caracter in msg_no_valido:
                print(caracter, end="", flush=True)
                sleep(0.02)

            input("\n| Presione enter para continuar:")
            
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|"+ " " * 80)

            linea = 17
            posicionar_linea(linea)
            for _ in range(4):
                print("|"+ " " * 80)

            for _ in range(4):
                print(LINE_UP, end="")

    linea = 23
    posicionar_linea(linea)
    print("|"+ " " * 40)

    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def imprimir_alternativas(alternativas):
    
    LINE_UP = '\033[1A'
    for clave, valor in alternativas.items():
        posibilidad = "| " + clave + ") " + valor[0]

        for caracter in posibilidad:
            print(caracter, end="", flush=True)
            sleep(0.02)

    linea = 22
    posicionar_linea(linea)
    for _ in range(2):
        print("|" + " " * 70)

    print(LINE_UP, end="")
    opcion = input("| Seleccione una opción:").lower().replace(" ", "")

    return opcion, alternativas

def imprimir_imagen(archivo_imagen):
    
    linea = 1
    posicionar_linea(linea)

    with open(archivo_imagen, 'r') as archivo:
        arte_ascii = archivo.read()

    for caracter in arte_ascii:
        print(caracter, end="", flush=True)
        sleep(0.005)
    
    linea = 23
    posicionar_linea(linea)

    input("| Presione enter para continuar:")

def posicionar_linea(linea):
    LINE_UP = '\033[1A'
    for _ in range(100):
        print(LINE_UP, end="")

    # Imprimir líneas vacías hasta alcanzar la línea actual
    for _ in range(linea):
        print("")

def imprimir_mensaje(linea_actual: int, 
                     cantidad_seccion: int, lista_secciones: list,
                     constante_linea, constante_rango):

    # Verificar si el mensaje en la sublista está activo para impresión
        if lista_secciones[-1][0] == True :

            borrar_pantalla( )

            # Mover el cursor y obtener la línea actual y rango de mensaje
            (linea_actual, 
             cantidad_seccion, constante_linea, 
             constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                              lista_secciones, constante_linea, 
                                                              constante_rango,)
            
            print("| ", end="")  # Imprimir el delimitador inicial de la línea
            
            # Iterar sobre cada palabra en la sección de escritura
            for caracter in lista_secciones[-1][1]:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Pausa breve para efecto de escritura

            borrar_pantalla( )

            # Ajustar la línea actual y rango de mensaje después de la impresión
            (linea_actual, 
                cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                                                                constante_rango)
            
            cantidad_seccion += constante_rango

            # Mover el cursor de nuevo para la siguiente palabra
            (linea_actual, 
                cantidad_seccion, constante_linea, 
                constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                                lista_secciones, constante_linea, 
                                                                constante_rango,)
            
            # Mover el cursor de nuevo para la siguiente palabra
            print("| ", end="")  # Imprimir el delimitador de la nueva línea

        #sleep(3) #SLEEP MUY IMPORTANTE
            (linea_actual, 
            cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                                                            constante_rango)

        else:
            borrar_pantalla( )

            (linea_actual, 
             cantidad_seccion, constante_linea, 
             constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                              lista_secciones, constante_linea,
                                                              constante_rango)
            
            print("|" + " " * 18, end="")
            # Iterar sobre cada palabra en la sección de escritura
            for caracter in lista_secciones[-1][1]:
                print(caracter, end="", flush=True)
                sleep(0.02)

            borrar_pantalla( )

            # Ajustar la línea actual y rango de mensaje después de la impresión
            (linea_actual, 
                cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                                                                constante_rango)

            cantidad_seccion += constante_rango

            # Mover el cursor de nuevo para la siguiente palabra
            (linea_actual, 
                cantidad_seccion, constante_linea, 
                constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                                lista_secciones, constante_linea, 
                                                                constante_rango,)

            (linea_actual, 
            cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                                                            constante_rango)

    # Retornar la línea actual y rango de mensaje actualizados
        return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def mover_cursor(linea_actual: int, cantidad_seccion: int, 
                 lista_secciones: list, 
                constante_linea, constante_rango):

    LINE_UP = '\033[1A'  # Secuencia de escape ANSI para mover el cursor arriba
    
    # Mover el cursor hacia arriba 100 líneas
    for _ in range(100):
        print(LINE_UP, end="")

    # Imprimir líneas vacías hasta alcanzar la línea actual
    for _ in range(linea_actual):

        # Si es la última línea y no es la 14, ajustar el rango del mensaje
        if _ == linea_actual - 1 and _ != 14:
            print("")
            cantidad_seccion, linea_actual = rango_seccion(lista_secciones, cantidad_seccion, linea_actual)
        

        else:
            print("")  # Imprimir línea vacía
    
    if _ == 0 and linea_actual == 1:

        (linea_actual, constante_linea, 
         constante_rango, lista_secciones) = verificar_linea(linea_actual, constante_linea, 
                                                             constante_rango, lista_secciones)

                                        

    # Devolver la línea actual y el rango de mensaje actualizados
    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def restar_linea(linea_actual, cantidad_seccion, constante_rango):

    if linea_actual != 1 and cantidad_seccion != 10:
        linea_actual -= 1

    elif linea_actual == 1 and cantidad_seccion == 7:
        linea_actual = 2
        constante_rango = 0


    return linea_actual, cantidad_seccion, constante_rango

def verificar_linea(linea_actual, constante_linea, constante_rango, lista_secciones):

    constante_linea = 0
    constante_rango = 0

    lista_secciones.pop(0)
    
    return linea_actual, constante_linea, constante_rango, lista_secciones

def rango_seccion(lista_secciones: list, cantidad_seccion: int, linea_actual):

    i = 0         # Inicializa el índice de la línea actual
    seccion = 0   # Inicializa el índice de la sección actual

    # Bucle para ajustar el rango de la sección a mostrar
    while i < cantidad_seccion :
        

        # Llama a imprimir_seccion para mostrar la sección actual
        seccion, i, lista_secciones = imprimir_seccion(lista_secciones, seccion, i)

            # Actualizar los índices para la próxima sección
        seccion += 1
        i += 1
    return cantidad_seccion, linea_actual  # Retorna el rango de mensaje ajustado

def imprimir_seccion(lista_secciones: list, seccion: int, i: int):
    
    # Imprimir la línea del mensaje según el estado activo
    if lista_secciones[seccion][0] == True:
        print("| " + lista_secciones[seccion][1] )
        

    else:
        print("| " + " " * 18 + lista_secciones[seccion][1])

    # Devolver los valores actualizados
    return seccion, i, lista_secciones

def borrar_pantalla( ):

    LINE_UP = '\033[1A'  # Secuencia de escape ANSI para mover el cursor hacia arriba
    
    # Mover el cursor hacia arriba 100 líneas
    for _ in range(100):
        print(LINE_UP, end="")

    print("")  # Imprimir una línea en blanco para separar el contenido

    # Imprimir líneas vacías para simular el borrado de la pantalla
    for _ in range(15):
        print("|" + " " * 80)

if __name__ == "__main__":
    
    # Limpiar la pantalla
    os.system('cls')

    linea_actual = imprimir_ventana( )
    obtener_mensajes_arcos(linea_actual)