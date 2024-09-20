import json
import os
from time import sleep
from copy import deepcopy

# Constante rango si es cero cuando se llega al borde superior

def imprimir_ventana( ):
    """
    Imprime una representación de una ventana de diálogo con una sección de
    interacción en la consola.
    

    Args:

        altura_dialogo (int): La altura de la sección de diálogo de la ventana.

        altura_interaccion (int): La altura de la sección de interacción de la
        ventana.
        
    Returns:
        None
    """
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
    with open("historia.json", "r", encoding="utf-8") as archivo:
        # Se lee el contenido del archivo
        contenido = archivo.read()

    # Se carga el contenido JSON en un diccionario de datos
    datos_lectura = json.loads(contenido)

    # Recorremos el diccionario de datos
    for _, contenido_arco in datos_lectura.items():

        contenido_mensajes = contenido_arco.get("mensajes")

        cantidad_seccion = 0

        for mensaje in contenido_mensajes:
            paquete_mensajes.append(mensaje)

        pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion)

    return paquete_mensajes

def pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion):

    lista_secciones = []

    constante_linea =  1
    constante_rango = 1

    for paquete in paquete_mensajes:

        orientacion_paquete = []

        mensaje_actual = (paquete.get("texto"))

        secciones_mensajes = dividir_mensaje(mensaje_actual)

        orientacion_paquete.append(paquete.get("orientacion"))
        orientacion_paquete.append(secciones_mensajes)

        lista_secciones.append(orientacion_paquete)

        (linea_actual, cantidad_seccion, 
         constante_linea, constante_rango) = imprimir_mensaje(secciones_mensajes, linea_actual, 
                                                              cantidad_seccion, lista_secciones, 
                                                              constante_linea, constante_rango)
        
        #Posiciona la opción presione para continuar donde debe de ser
        LINE_UP = '\033[1A'

        for _ in range(100):
            print(LINE_UP, end="")

        # Imprimir líneas vacías hasta alcanzar la línea actual
        for _ in range(23):
            print("")
        input("| Presione enter para continuar:")

def dividir_mensaje(mensaje_actual: str):
    secciones_mensajes = []
    ancho_texto = 60

    while len(mensaje_actual) > ancho_texto:

        indice = mensaje_actual[:ancho_texto].rfind(" ")

        if indice == -1: 
            indice = ancho_texto
        secciones_mensajes.append(mensaje_actual[:indice])
        mensaje_actual = mensaje_actual[indice:].lstrip()

    secciones_mensajes.append(mensaje_actual)

    return secciones_mensajes

def imprimir_mensaje(secciones_mensajes: list, linea_actual: int, 
                     cantidad_seccion: int, lista_secciones: list,
                     constante_linea, constante_rango):

    # Verificar si el mensaje en la sublista está activo para impresión
        if lista_secciones[-1][0] == True :
            # print(f"seccion en específico {lista_secciones[0][1][0]}")
            # print(f"longitud mensajes {len(lista_secciones[0][1])}")
            # sleep(3)

            borrar_pantalla( )

            # Mover el cursor y obtener la línea actual y rango de mensaje
            (linea_actual, 
             cantidad_seccion, constante_linea, 
             constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                              lista_secciones, constante_linea, 
                                                              constante_rango,)
            
            print("| ", end="")  # Imprimir el delimitador inicial de la línea
            
            # Iterar sobre cada palabra en la sección de escritura
            for palabra in secciones_mensajes:
                
                # Imprimir cada carácter de la palabra con un efecto de escritura
                for caracter in palabra:
                    print(caracter, end="", flush=True)
                    sleep(0.02)  # Pausa breve para efecto de escritura

                # print(f"                                                                            {lista_secciones}")

                # sleep(3) 

                borrar_pantalla( )

                # Ajustar la línea actual y rango de mensaje después de la impresión
                # (linea_actual, 
                #  cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                #                                                    constante_rango)
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
            # (linea_actual, 
            #  cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
            #                                                    constante_rango)
            # print(f"                                                                                   lc{linea_actual} cs{cantidad_seccion}")

        else:
            borrar_pantalla( )

            #linea_actual -= 1
            #cantidad_seccion -= 1
            # Mover el cursor y obtener la línea actual y rango de mensaje
            (linea_actual, 
             cantidad_seccion, constante_linea, 
             constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                              lista_secciones, constante_linea,
                                                              constante_rango)
            # Iterar sobre cada palabra en la sección de escritura
            for seccion in secciones_mensajes:
                print("|" + " " * 18, end="")  # Imprimir espacio inicial

                # Imprimir cada carácter de la palabra con un efecto de escritura
                for caracter in seccion:
                    print(caracter, end="", flush=True)
                    sleep(0.02)  # Pausa breve para efecto de escritura
                # print(f"                                                                            {lista_secciones}")

                # sleep(3) 

                borrar_pantalla( )

                # Ajustar la línea actual y rango de mensaje después de la impresión
                # (linea_actual, 
                #  cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
                #                                                    constante_rango)
                cantidad_seccion += constante_rango

                # Mover el cursor de nuevo para la siguiente palabra
                (linea_actual, 
                 cantidad_seccion, constante_linea, 
                 constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                                  lista_secciones, constante_linea, 
                                                                  constante_rango,)

            # (linea_actual, 
            #  cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion, 
            #                                                    constante_rango)

    # Retornar la línea actual y rango de mensaje actualizados
        return linea_actual, cantidad_seccion, constante_linea, constante_rango

def restar_linea(linea_actual, cantidad_seccion):

    if linea_actual != 1:
        linea_actual -= 1

    return linea_actual, cantidad_seccion

def verificar_linea(linea_actual, constante_linea, constante_rango, 
                    lista_secciones, cantidad_seccion):

    constante_linea = 0
    constante_rango = 0

    lista_secciones[0][1].pop(0)

    #Si el paquete ya está vacio se borra el paquete
    if len(lista_secciones[0][1]) == 0:

        lista_secciones.pop(0)

        contador = 0

        for paquete in range(len(lista_secciones)):
            contador += len(lista_secciones[paquete][1])

        cantidad_seccion = contador - 1
        print(f"                                                                                                {linea_actual}")
        linea_actual = 2
        print(f"                                                                                                {linea_actual}")

    return linea_actual, constante_linea, constante_rango, lista_secciones, cantidad_seccion

def mover_cursor(linea_actual: int, cantidad_seccion: int, lista_secciones: list, 
                 constante_linea, constante_rango):
    """
    Mueve el cursor hacia arriba en la consola y ajusta el rango del mensaje.
    
    Args:
        linea_actual (int): La línea actual desde donde se moverá el cursor.

        cantidad_seccion (int): El rango actual del mensaje en la lista de mensajes.

        lista_mensajes (list): Lista de mensajes que se está procesando.

    Returns:
        tuple: Una tupla que contiene la línea actual y el rango de mensaje 
        actualizados.
    """
    if cantidad_seccion != 0:
        
        (linea_actual, cantidad_seccion) = restar_linea(linea_actual, cantidad_seccion)
        # print(f"                                                                                             LIN{linea_actual}CAN{cantidad_seccion}")
        
    
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

        (linea_actual, 
         constante_linea, constante_rango, 
         lista_secciones, cantidad_seccion) = verificar_linea(linea_actual, constante_linea, 
                                                             constante_rango, lista_secciones, 
                                                             cantidad_seccion)

                                        
    # sleep(3)
    # Devolver la línea actual y el rango de mensaje actualizados
    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def rango_seccion(lista_secciones: list, cantidad_seccion: int, linea_actual):
    """
    Ajusta el rango del mensaje a mostrar en la pantalla.

    Args:
        lista_mensajes (list): Lista de listas que contiene los mensajes y 
        sus respectivas secciones.

        cantidad_seccion (int): Rango actual del mensaje a ser impreso.

    Returns:
        int: El rango del mensaje actual después de ajustar la sección.
    """
    contador = 0  # Inicializa el contador para recorrer los mensajes
    i = 0         # Inicializa el índice de la línea actual
    seccion = 0   # Inicializa el índice de la sección actual

    # Bucle para ajustar el rango de la sección a mostrar
    while i < cantidad_seccion :
        #and contador < len(lista_secciones)
        # print("---------------------------------------------------------------------------------------------------------")
        # print(f"                                                   {lista_secciones}")
        
        #print(f"                                                                                       c{contador} f{seccion} s{seccion} i{i} l{linea_actual} r{cantidad_seccion} ")
        # print("---------------------------------------------------------------------------------------------------------")
        # sleep(2)
        
        # Comprueba si hay más secciones en el mensaje actual
        if seccion < len(lista_secciones[contador][1]):

            # Llama a imprimir_seccion para mostrar la sección actual
            seccion, i, contador, lista_secciones = imprimir_seccion(lista_secciones, contador, 
                                                                     seccion, i)

        else:
            # Si no hay más secciones, imprime una línea vacía y avanza al
            # siguiente
            contador += 1  # Avanza al siguiente mensaje
            seccion = 0    # Reinicia el índice de la sección

    return cantidad_seccion, linea_actual  # Retorna el rango de mensaje ajustado

def imprimir_seccion(lista_secciones: list, contador: int, seccion: int, i: int):
    
    """
    Imprime una sección de un mensaje basado en el estado actual y parámetros.

    Args:
        lista_mensajes (list): Lista de listas que contiene los mensajes y 
        su estado de visualización.

        contador (int): Índice del mensaje en la lista que se está procesando.

        seccion (int): Índice de la sección actual dentro del mensaje.

        i (int): Línea actual en la pantalla donde se imprimirá el mensaje.

    Returns:
        tuple: Una tupla que contiene los valores actualizados
               seccion, i, contador y lista_mensajes.
    """
    
    # Imprimir la línea del mensaje según el estado activo
    if lista_secciones[contador][0] == True:
        print("| " + lista_secciones[contador][1][seccion] )
        

    else:
        print("| " + " " * 18 + lista_secciones[contador][1][seccion])
        

    # Actualizar los índices para la próxima sección
    seccion += 1
    i += 1
    

    # Devolver los valores actualizados
    return seccion, i, contador, lista_secciones

def borrar_pantalla( ):
    """
    Borra el contenido de la pantalla simulando un efecto de desplazamiento.
    
    Args:

    Returns:
        None
    """
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

    lista_mensajes = obtener_mensajes_arcos(linea_actual)

