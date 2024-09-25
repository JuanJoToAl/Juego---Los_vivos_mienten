import json  # Importa el módulo para manejar datos en formato JSON
from time import sleep  # Importa la función sleep para pausas en el tiempo
import os    # Importa el módulo para interactuar con el sistema operativo
from modulo_impresion import *

def obtener_mensajes_arcos(linea_actual: int):
    """

    Esta función lee los mensajes de diferentes arcos narrativos,
    los almacena en una lista y los presenta al usuario. Se encarga
    de gestionar el avance a través de los arcos y de interactuar
    con el juego según la progresión del usuario.
    
    Args:
        linea_actual (int): La línea actual para la interacción.
    
    Returns:
        list: Una lista de mensajes obtenidos de los arcos.
    """

    paquete_mensajes = []  # Lista para almacenar los mensajes obtenidos.
    
    # Abre el archivo "historia_prueba.json" en modo lectura.
    with open("historia_prueba.json", "r", encoding="utf-8") as archivo:

        # Lee el contenido del archivo.
        contenido = archivo.read()
    
    # Carga el contenido JSON en un diccionario de datos.
    datos_lectura = json.loads(contenido)
    
    contador_arcos = 0  # Inicializa el contador de arcos.
    nombres_arcos = list(datos_lectura.keys())  # Obtiene los nombres de arcos.
    lista_avance = []  # Lista para almacenar el avance en los arcos.
    arco_actual = nombres_arcos[contador_arcos]  # Arco actual a procesar.
    
    while contador_arcos < len(nombres_arcos):
        # Imprime el nombre del arco actual.
        imprimir_nombre_arco(arco_actual)
        lista_avance.append(arco_actual)  # Agrega el arco actual a la lista.
        
        contenido_mensajes = datos_lectura[arco_actual].get("mensajes")
        cantidad_seccion = 0  # Inicializa la cantidad de secciones.
        
        paquete_mensajes = []  # Reinicia la lista de mensajes.
        
        # Almacena los mensajes del arco actual.
        for mensaje in contenido_mensajes:
            paquete_mensajes.append(mensaje)
        
        # Pasa la información de los mensajes.
        pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion)
        
        contador_arcos += 1  # Incrementa el contador de arcos.
        
        bandera_arco = True  # Bandera para indicar el estado del arco.
        
        # Llama a la función para verificar el estado del juego.
        (bandera_arco,
         contador_arcos, nombres_arcos) = terminar_juego(bandera_arco, 
                                                         contador_arcos,
                                                         nombres_arcos)
        
        while bandera_arco == True:
            # Restaura el arco actual si es necesario.
            (arco_actual, lista_avance,
             contador_arcos, bandera_arco) = restaurar_arco(contador_arcos, 
                                                            lista_avance,
                                                            arco_actual, 
                                                            nombres_arcos,
                                                            bandera_arco)
    
    linea = 22  # Establece la línea para el mensaje final.
    posicionar_linea(linea)  # Posiciona la línea en la salida.
    
    # Imprime líneas vacías para el formato.
    for _ in range(2):
        print("|" + " " * 80)
    
    linea = 1  # Reinicia la línea para el mensaje final.
    posicionar_linea(linea)  
    
    mensaje_final = ("| Gracias por jugar. ¡Hasta la próxima!\n\n"
                     "| Créditos:\n| Programado y escrito por:"
                     " Juan José Tobar y Jospeh Lievano")
    
    # Imprime el mensaje final carácter por carácter.
    for caracter in mensaje_final:
        print(caracter, end="", flush=True)
        sleep(0.03)  # Agrega un pequeño retardo entre caracteres.
    
    linea = 26  # Establece la línea final para el formato.
    posicionar_linea(linea)  
    
    return paquete_mensajes  # Devuelve la lista de mensajes obtenidos.

def terminar_juego(bandera_arco: bool, 
                   contador_arcos: int, 
                   nombres_arcos: list) -> tuple:
    """
    Controla el cierre del juego basado en la respuesta del usuario, 
    verificando si el usuario desea finalizar o continuar con el 
    progreso de los arcos narrativos.

    Args:
        bandera_arco (bool): Indica si el arco actual está activo.
        contador_arcos (int): Contador de arcos procesados.
        nombres_arcos (list): Lista de nombres de arcos disponibles.
    
    Returns:
        tuple: Nueva bandera de arco, contador de arcos y nombres de arcos.
    """
    LINE_UP = '\033[1A'  # Control para mover el cursor hacia arriba.
    marcador = True  # Marca para seguir mostrando el menú.
    
    # Ciclo principal que controla la interacción del usuario.
    while bandera_arco == True and marcador == True:
        linea = 22  # Línea para posicionar el menú.
        posicionar_linea(linea)  # Posiciona la línea en la salida.
        
        # Imprime espacios en blanco para el formato.
        for _ in range(2):
            print("|" + " " * 80)
        for _ in range(2):
            print(LINE_UP, end="")  # Mueve el cursor hacia arriba.

        # Solicita al usuario si desea cerrar el juego.
        respuesta = input("| ¿Quiere cerrar el juego? (si ; no):")
        
        # Verifica si la respuesta es "si".
        if respuesta.lower().replace(" ", "") == "si":
            bandera_arco = False  # Cambia el estado del arco a inactivo.
            marcador = False  # Detiene el ciclo.
            contador_arcos = len(nombres_arcos)  # Marca todos los arcos como procesados.
        
        # Verifica si la respuesta es "no".
        elif respuesta.lower().replace(" ", "") == "no":
            bandera_arco = True  # Mantiene el arco activo.
            marcador = False  # Detiene el ciclo.
        
        # Maneja respuestas no válidas.
        else:
            linea = 22  # Posiciona la línea en la salida.
            posicionar_linea(linea)  # Ajusta la línea.
            
            # Imprime espacios en blanco para el formato.
            for _ in range(2):
                print("|" + " " * 80)
            for _ in range(2):
                print(LINE_UP, end="")  # Mueve el cursor hacia arriba.

            msg_no_valido = "| Seleccione una opción válida"  # Mensaje de error.
            # Imprime el mensaje de error carácter por carácter.
            for caracter in msg_no_valido:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Agrega un pequeño retardo entre caracteres.

            input("\n| Presione enter para continuar:")  # Espera entrada del usuario.

    return bandera_arco, contador_arcos, nombres_arcos  # Devuelve el estado final.

def restaurar_arco(contador_arcos: int, lista_avance: list, 
                   arco_actual: str, nombres_arcos: list, bandera_arco: bool) -> tuple:
    """   
    Permite al usuario regresar a un arco  de la historia, actualizando el
    progreso y el estado del arco. También verifica si el arco deseado es
    accesible y maneja el flujo de la narrativa según la decisión del usuario.
    
    Args:
        contador_arcos (int): Contador de arcos procesados.
        lista_avance (list): Lista de arcos avanzados por el usuario.
        arco_actual (str): Arco actual en el que se encuentra el usuario.
        nombres_arcos (list): Lista de nombres de arcos disponibles.
        bandera_arco (bool): Indica si el arco actual está activo.
    
    Returns:
        tuple: Arco actual, lista de avance, contador de arcos y bandera.
    """
    LINE_UP = '\033[1A'  # Control para mover el cursor hacia arriba.

    linea = 22  # Línea para posicionar el menú.
    posicionar_linea(linea)  # Posiciona la línea en la salida.
    
    # Imprime espacios en blanco para el formato.
    for _ in range(2):
        print("|" + " " * 80)
    for _ in range(2):
        print(LINE_UP, end="")  # Mueve el cursor hacia arriba.

    # Solicita al usuario si desea regresar a un arco anterior.
    respuesta = input("| ¿Quiere regresar a un arco? (si ; no):")

    # Verifica si la respuesta es "si".
    if respuesta.lower().replace(" ", "") == "si":
        punto_retroceso = input("| ¿A cuál arco quiere regresar?:")

        # Verifica si el arco de retroceso está en la lista de avance.
        if punto_retroceso.lower().replace(" ", "") in lista_avance:
            arco_actual = punto_retroceso.lower().replace(" ", "")
            # Actualiza el contador de arcos al índice del arco de retroceso.
            contador_arcos = lista_avance.index(punto_retroceso.lower().replace(" ", ""))

            linea = 22  # Línea para limpiar la salida.
            posicionar_linea(linea)
            print("|" + " " * 80)
            print("|" + " " * 80)

            bandera_arco = False  # Marca el arco como inactivo.

        else:
            linea = 22  # Posiciona la línea en la salida.
            posicionar_linea(linea)
            # Imprime espacios en blanco para el formato.
            for _ in range(2):
                print("|" + " " * 80)
            for _ in range(2):
                print(LINE_UP, end="")  # Mueve el cursor hacia arriba.

            msg_no_hallado = "| La solicitud no se encuentra disponible"  # Mensaje de error.

            # Imprime el mensaje de error carácter por carácter.
            for caracter in msg_no_hallado:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Agrega un pequeño retardo entre caracteres.

            input("\n| Presione enter para continuar:")  # Espera entrada del usuario.

    # Verifica si la respuesta es "no" y si hay arcos disponibles.
    elif (respuesta.lower().replace(" ", "") == "no"
          and contador_arcos < len(nombres_arcos)):
        arco_actual = nombres_arcos[contador_arcos]  # Actualiza el arco actual.

        linea = 22  # Línea para limpiar la salida.
        posicionar_linea(linea)
        print("|" + " " * 80)

        bandera_arco = False  # Marca el arco como inactivo.

    # Si se han procesado todos los arcos, se desactiva la bandera.
    elif contador_arcos == len(nombres_arcos):
        bandera_arco = False  # Desactiva el arco.

    else:
        None  # No se realiza ninguna acción.

    return arco_actual, lista_avance, contador_arcos, bandera_arco  # Devuelve el estado final.

def pasar_informacion(paquete_mensajes: list, 
                      linea_actual: int, cantidad_seccion: int) -> None:
    """
    La función recorre cada paquete de mensajes y lo muestra en pantalla.
    También gestiona la impresión de imágenes y alternativas según el contenido
    del paquete.
    
    Args:
        paquete_mensajes (list): Lista de mensajes a procesar.
        linea_actual (int): Línea actual en la que se está mostrando el mensaje.
        cantidad_seccion (int): Cantidad de secciones mostradas.

    Returns:
        None
    """
    lista_secciones = []  # Lista para almacenar secciones de mensajes.

    constante_linea = 1  # Constante para la línea de impresión.
    constante_rango = 1  # Constante para el rango de impresión.

    # Procesa cada paquete de mensajes en la lista.
    for paquete in paquete_mensajes:
        orientacion_paquete = []  # Lista para almacenar orientación del paquete.

        mensaje_actual = (paquete.get("texto"))  # Obtiene el texto del mensaje.

        # Agrega la orientación y el mensaje a la lista de secciones.
        orientacion_paquete.append(paquete.get("orientacion"))
        orientacion_paquete.append(mensaje_actual)
        lista_secciones.append(orientacion_paquete)

        # Imprime el mensaje y actualiza las variables.
        (linea_actual, cantidad_seccion,
         constante_linea, constante_rango, lista_secciones) = imprimir_mensaje(linea_actual, cantidad_seccion, 
                                                                               lista_secciones, constante_linea, 
                                                                               constante_rango)

        linea = 23  # Línea para posicionar el siguiente mensaje.
        posicionar_linea(linea)  # Posiciona la línea en la salida.

        input("| Presione enter para continuar:")  # Espera entrada del usuario.

        # Si hay una imagen en el paquete, la imprime.
        if paquete.get("imagen"):
            archivo_imagen = paquete.get("imagen")  # Obtiene la imagen.
            borrar_pantalla()  # Limpia la pantalla.
            imprimir_imagen(archivo_imagen)  # Imprime la imagen.

        # Si hay alternativas en el paquete, las procesa.
        if paquete.get("alternativas"):
            alternativas = paquete.get("alternativas")  # Obtiene las alternativas.

            # Procesa las alternativas y actualiza las variables.
            (linea_actual, cantidad_seccion,
             constante_linea, constante_rango, lista_secciones) = recorrer_alternativas(alternativas, linea_actual, 
                                                                                        cantidad_seccion, constante_linea, constante_rango, lista_secciones)

    borrar_pantalla()  # Limpia la pantalla al finalizar.

def recorrer_alternativas(alternativas: dict, linea_actual: int, 
                          cantidad_seccion: int, constante_linea: int, 
                          constante_rango: int, lista_secciones: list) -> tuple:
    """
    Procesa las alternativas seleccionadas por el usuario y muestra
    los mensajes correspondientes. También permite al usuario elegir entre
    múltiples opciones y actualiza el estado del programa según la
    selección realizada.

    Args:
        alternativas (dict): Opciones disponibles para el usuario.
        linea_actual (int): Línea actual en la que se muestra el mensaje.
        cantidad_seccion (int): Cantidad de secciones mostradas.
        constante_linea (int): Valor constante para manejar líneas.
        constante_rango (int): Valor constante para manejar rangos.
        lista_secciones (list): Lista de secciones de mensajes.

    Returns:
        tuple: Valores actualizados de linea_actual, cantidad_seccion,
               constante_linea, constante_rango y lista_secciones.
    """
    LINE_UP = '\033[1A'  # Control de línea para mover el cursor hacia arriba.

    # Posiciona la opción "Presione para continuar" donde debe ser.
    linea = 17
    posicionar_linea(linea)

    # Procesa mientras haya alternativas disponibles.
    while len(alternativas) != 0:
        # Imprime las alternativas y obtiene la opción seleccionada.
        opcion, alternativas = imprimir_alternativas(alternativas)

        if opcion in alternativas:
            lista_auxiliar = []  # Lista para almacenar la opción seleccionada.
            lista_auxiliar.append(False)  # Estado de la opción.
            lista_auxiliar.append(alternativas[opcion][1])  # Mensaje.

            lista_secciones.append(lista_auxiliar)  # Agrega a secciones.

            # Imprime el mensaje y actualiza las variables.
            (linea_actual, cantidad_seccion,
            constante_linea, constante_rango, lista_secciones) = imprimir_mensaje(linea_actual, cantidad_seccion, 
                                                                                  lista_secciones,constante_linea, 
                                                                                  constante_rango)

            del alternativas[opcion]  # Elimina la opción seleccionada.

            linea = 17  # Restablece la línea para la siguiente impresión.
            posicionar_linea(linea)

            # Limpia el área de impresión para mostrar el siguiente mensaje.
            for _ in range(4):
                print("|" + " " * 80)

            for _ in range(4):
                print(LINE_UP, end="")

        else:
            # Mensaje de opción no válida y espera la entrada del usuario.
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|" + " " * 80)

            for _ in range(2):
                print(LINE_UP, end="")

            msg_no_valido = "| Seleccione una opcion válida"
            for caracter in msg_no_valido:
                print(caracter, end="", flush=True)
                sleep(0.02)  # Retardo entre caracteres.

            input("\n| Presione enter para continuar:")

            # Limpia la pantalla y vuelve a la selección de alternativas.
            linea = 22
            posicionar_linea(linea)
            for _ in range(2):
                print("|" + " " * 80)

            linea = 17
            posicionar_linea(linea)
            for _ in range(4):
                print("|" + " " * 80)

            for _ in range(4):
                print(LINE_UP, end="")

    linea = 23  # Prepara la línea para finalizar el proceso.
    posicionar_linea(linea)
    print("|" + " " * 40)  # Espacio final para el mensaje.

    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

if __name__ == "__main__":

    # Limpiar la pantalla para una mejor visualización
    os.system('cls')

    # Obtener la línea actual para imprimir la ventana
    linea_actual = imprimir_ventana()

    # Cargar y mostrar los mensajes de los arcos
    obtener_mensajes_arcos(linea_actual)