import os
from time import sleep
from copy import deepcopy


def imprimir_ventana(ancho_pantalla : int, altura_dialogo : int, 
                     altura_interaccion: int):
    """
    Imprime una representación de una ventana de diálogo con una sección de
    interacción en la consola.
    

    Args:
        ancho_pantalla (int): El ancho de la ventana.

        altura_dialogo (int): La altura de la sección de diálogo de la ventana.

        altura_interaccion (int): La altura de la sección de interacción de la
        ventana.
        
    Returns:
        None
    """
    # Imprimir la línea superior de la ventana
    print("-" * (ancho_pantalla + 2))
    
    # Imprimir la sección de diálogo de la ventana
    for _ in range(altura_dialogo):
        print("|" + " " * ancho_pantalla + "|")
    
    # Imprimir la línea divisoria entre la sección de diálogo y la de interacción
    print("-" * (ancho_pantalla + 2))
    
    # Imprimir la sección de interacción de la ventana
    for _ in range(altura_interaccion):
        print("|" + " " * ancho_pantalla + "|")
    
    # Imprimir la línea inferior de la ventana
    print("-" * (ancho_pantalla + 2))


def dividir_mensaje(lista_mensajes: list, ancho_pantalla: int,
                    sublista: int, seccion_escritura: list):
    """
    Divide un mensaje en secciones según el ancho de pantalla disponible.

    Args:
        lista_mensajes (list): Lista de listas que contiene mensajes.

        ancho_pantalla (int): El ancho de la pantalla para ajustar el texto.

        sublista (int): Índice de la sublista que contiene el mensaje a dividir.

        seccion_escritura (list): Lista donde se almacenarán las secciones del 
        mensaje dividido.

    Returns:
        tuple: Contiene la lista de secciones del mensaje dividido y la lista 
        de mensajes actualizada.
    """
    # Obtener el mensaje de la sublista especificada
    mensaje = lista_mensajes[sublista][1]
    
    # Eliminar el mensaje original de la sublista
    lista_mensajes[sublista].remove(lista_mensajes[sublista][1])
    
    # Inicializar la lista para almacenar las secciones del mensaje
    seccion_escritura = []
    
    # Calcular el ancho máximo del texto permitido en una línea
    ancho_texto = ancho_pantalla - 20
    
    # Inicializar contadores para recorrer el mensaje
    recorrido = 0
    contador = 0
    
    # Bandera para controlar el bucle de división
    bandera = True

    # Bucle para dividir el mensaje en secciones según el ancho de texto
    while recorrido < len(mensaje) and bandera:
        # Guardar el índice del último espacio antes del límite de ancho
        if mensaje[contador] == " " and contador < ancho_texto:
            indice = contador
        
        # Si se alcanza el ancho de texto, cortar mensaje y agregar a lista
        elif ancho_texto <= contador:
            seccion_escritura.append(mensaje[:indice])
            mensaje = mensaje[indice:].lstrip()  # Eliminar espacios al inicio
            recorrido = 0
            contador = 0
        
        # Si el mensaje restante es menor que el ancho de texto, agregar a la
        # lista
        
        elif len(mensaje) < ancho_texto:
            seccion_escritura.append(mensaje)
            bandera = False
        
        recorrido += 1
        contador += 1

    # Agregar las secciones del mensaje dividido a la sublista correspondiente
    lista_mensajes[sublista].append(seccion_escritura)

    # Devolver la lista de secciones y la lista de mensajes actualizada
    return seccion_escritura, lista_mensajes

def imprimir_mensaje(seccion_escritura: list, lista_mensajes: list, linea_actual: int,
                     ancho_pantalla: int, sublista: int, rango_mensaje: int):
    """
    Imprime un mensaje sección por sección con un efecto de escritura.

    Args:
        seccion_escritura (list): Lista de secciones de texto a imprimir.

        lista_mensajes (list): Lista de listas que contiene los mensajes y
        su estado de visualización.

        linea_actual (int): Línea actual en la pantalla donde se imprimirá.

        ancho_pantalla (int): Ancho de la pantalla para ajustar el texto.

        sublista (int): Índice de la sublista en 'lista_mensajes' que contiene 
        el mensaje a imprimir.

        rango_mensaje (int): Rango del mensaje a imprimir en la pantalla.

    Returns:
        tuple: Una tupla que contiene la línea actual y el rango de mensaje
        actualizados.
    """
    
    # Verificar si el mensaje en la sublista está activo para impresión
    if lista_mensajes[sublista][0] == True:

        # Mover el cursor y obtener la línea actual y rango de mensaje
        linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje,
                                                   lista_mensajes)
        
        print("| ", end="")  # Imprimir el delimitador inicial de la línea

        # Iterar sobre cada palabra en la sección de escritura
        for palabra in seccion_escritura:

            # Imprimir cada carácter de la palabra con un efecto de escritura
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Pausa breve para efecto de escritura
            
            # Borrar la pantalla después de imprimir una palabra
            borrar_pantalla(ancho_pantalla)

            # Ajustar la línea actual y rango de mensaje después de la impresión
            linea_actual -= 1
            rango_mensaje -= 1

            # Mover el cursor de nuevo para la siguiente palabra
            linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje,
                                                       lista_mensajes)
            print("| ", end="")  # Imprimir el delimitador de la nueva línea

    else:
        # Si el mensaje no está activo, borrar la pantalla
        borrar_pantalla(ancho_pantalla)
        linea_actual -= 1

        # Mover el cursor y obtener la línea actual y rango de mensaje
        linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje,
                                                   lista_mensajes)
        print('\n', end="")  # Mover a la nueva línea sin imprimir nada

        # Iterar sobre cada palabra en la sección de escritura
        for palabra in seccion_escritura:
            print("|" + " " * 18, end="")  # Imprimir espacio inicial

            # Imprimir cada carácter de la palabra con un efecto de escritura
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Pausa breve para efecto de escritura

            # Borrar la pantalla después de imprimir una palabra
            borrar_pantalla(ancho_pantalla)

            # Ajustar la línea actual y rango de mensaje después de la impresión
            linea_actual -= 1
            rango_mensaje -= 1

            # Mover el cursor de nuevo para la siguiente palabra
            linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje,
                                                       lista_mensajes)

    # Retornar la línea actual y rango de mensaje actualizados
    return linea_actual, rango_mensaje

def mover_cursor(linea_actual: int, rango_mensaje: int, lista_mensajes: list):
    """
    Mueve el cursor hacia arriba en la consola y ajusta el rango del mensaje.
    
    Args:
        linea_actual (int): La línea actual desde donde se moverá el cursor.

        rango_mensaje (int): El rango actual del mensaje en la lista de mensajes.

        lista_mensajes (list): Lista de mensajes que se está procesando.

    Returns:
        tuple: Una tupla que contiene la línea actual y el rango de mensaje 
        actualizados.
    """
    LINE_UP = '\033[1A'  # Secuencia de escape ANSI para mover el cursor arriba

    # Mover el cursor hacia arriba 100 líneas
    for _ in range(100):
        print(LINE_UP, end="")

    # Imprimir líneas vacías hasta alcanzar la línea actual
    for _ in range(linea_actual):
        # Si es la última línea y no es la 14, ajustar el rango del mensaje
        if _ == linea_actual - 1 and _ != 14:
            print("")  # Imprimir línea vacía
            rango_mensaje = rango_seccion(lista_mensajes, rango_mensaje)
        else:
            print("")  # Imprimir línea vacía

    # Devolver la línea actual y el rango de mensaje actualizados
    return linea_actual, rango_mensaje

def rango_seccion(lista_mensajes: list, rango_mensaje: int):
    """
    Ajusta el rango del mensaje a mostrar en la pantalla.

    Args:
        lista_mensajes (list): Lista de listas que contiene los mensajes y 
        sus respectivas secciones.

        rango_mensaje (int): Rango actual del mensaje a ser impreso.

    Returns:
        int: El rango del mensaje actual después de ajustar la sección.
    """
    contador = 0  # Inicializa el contador para recorrer los mensajes
    frase = 0     # Inicializa el índice de la frase actual
    i = 0         # Inicializa el índice de la línea actual
    seccion = 0   # Inicializa el índice de la sección actual
   
    # Bucle para ajustar el rango de la sección a mostrar
    while i < 15 - rango_mensaje:

        # Comprueba si hay más secciones en el mensaje actual
        if seccion < len(lista_mensajes[contador][1]):

            # Llama a imprimir_seccion para mostrar la sección actual
            frase, seccion, i, contador, lista_mensajes = imprimir_seccion(
                lista_mensajes, contador, frase, seccion, i)
        else:
            # Si no hay más secciones, imprime una línea vacía y avanza al siguiente
            print("| " + " " * 18)

            contador += 1  # Avanza al siguiente mensaje
            frase = 0      # Reinicia el índice de la frase
            seccion = 0    # Reinicia el índice de la sección
   
    return rango_mensaje  # Retorna el rango de mensaje ajustado

def imprimir_seccion(lista_mensajes: list, contador: int, frase: int, 
                     seccion: int, i: int):
    """
    Imprime una sección de un mensaje basado en el estado actual y parámetros.

    Args:
        lista_mensajes (list): Lista de listas que contiene los mensajes y 
        su estado de visualización.

        contador (int): Índice del mensaje en la lista que se está procesando.
        
        frase (int): Índice de la frase dentro del mensaje actual.

        seccion (int): Índice de la sección actual dentro del mensaje.

        i (int): Línea actual en la pantalla donde se imprimirá el mensaje.

    Returns:
        tuple: Una tupla que contiene los valores actualizados de frase, 
               seccion, i, contador y lista_mensajes.
    """
    # Imprimir la línea del mensaje según el estado activo
    if lista_mensajes[contador][0] == True:
        print("| " + lista_mensajes[contador][1][frase])
    else:
        print("| " + " " * 18 + lista_mensajes[contador][1][frase])

    # Actualizar los índices para la próxima sección
    frase += 1
    seccion += 1
    i += 1

    # Devolver los valores actualizados
    return frase, seccion, i, contador, lista_mensajes

def borrar_pantalla(ancho_pantalla: int):
    """
    Borra el contenido de la pantalla simulando un efecto de desplazamiento.
    
    Args:
        ancho_pantalla (int): El ancho de la pantalla para ajustar el número de
        espacios en blanco impresos.

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
        print("|" + " " * ancho_pantalla)

if __name__ == "__main__":

    ancho_pantalla = 80  # Definir el ancho de la pantalla
    altura_dialogo = 15  # Altura del área de diálogo
    altura_interaccion = 8  # Altura del área de interacción

    # Copiar valores para el seguimiento de la línea actual y rango del mensaje
    linea_actual = deepcopy(altura_dialogo)
    rango_mensaje = deepcopy(linea_actual)

    # Limpiar la pantalla
    os.system('cls')

    # Imprimir el marco de la ventana
    imprimir_ventana(ancho_pantalla, altura_dialogo, altura_interaccion)

    # Lista de mensajes a procesar
    lista_mensajes = [
        [True, "[Serpiente]: Muchos años después, frente al pelotón de fusilamiento, el "
               "coronel Aureliano Buendía había de recordar aquella tarde remota en que "
               "su padre lo llevó a conocer el hielo."],
        [False, "[Serpiente]: La tierra, recién salida del barro, olía a hierba húmeda. Aureliano Buendía sintió el frío de la madrugada y se arrepintió de haber abandonado el sueño. Pero Úrsula, que era más práctica, le ordenó que fuera a reconocer los límites de la propiedad. Aureliano Buendía salió a galope, con las espuelas clavadas en los flancos del caballo, y regresó a mediodía con los ojos enrojecidos por el sol, la ropa hecha jirones y la frente surcada de sudor. Traía consigo la certeza de que habían llegado al fin del mundo."]
    ]
   
    sublista = 0  # Índice de la sublista actual en lista_mensajes
    seccion_escritura = []  # Lista para almacenar las secciones del mensaje

    # Dividir el mensaje en secciones para imprimir
    seccion_escritura, lista_mensajes = dividir_mensaje(
        lista_mensajes, ancho_pantalla, sublista, seccion_escritura
    )

    # Imprimir el mensaje sección por sección
    linea_actual, rango_mensaje = imprimir_mensaje(
        seccion_escritura, lista_mensajes, linea_actual, ancho_pantalla, sublista, rango_mensaje
    )

    # Avanzar a la siguiente sublista
    sublista += 1

    # Dividir el siguiente mensaje en secciones para imprimir
    seccion_escritura, lista_mensajes = dividir_mensaje(
        lista_mensajes, ancho_pantalla, sublista, seccion_escritura
    )

    # Imprimir el siguiente mensaje sección por sección
    linea_actual, rango_mensaje = imprimir_mensaje(
        seccion_escritura, lista_mensajes, linea_actual, ancho_pantalla, sublista, rango_mensaje
    )

    



