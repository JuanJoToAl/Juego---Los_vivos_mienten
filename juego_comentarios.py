import json  # Importa el módulo para manejar datos en formato JSON
import os    # Importa el módulo para interactuar con el sistema operativo
from time import sleep  # Importa la función sleep para pausas en el tiempo
from copy import deepcopy  # Importa deepcopy para copiar objetos complejos

def imprimir_ventana():
    """
    Imprime una ventana gráfica de diálogo e interacción en la terminal.
    
    Args:
        No recibe argumentos.
    
    Returns:
        int: La altura del área de diálogo de la ventana.
    """
    altura_dialogo = 15  # Altura de la sección de diálogo.
    altura_interaccion = 8  # Altura de la sección de interacción.
    
    # Copia la altura de la sección de diálogo.
    linea_actual = deepcopy(altura_dialogo)
    
    # Imprime la línea superior de la ventana.
    print("-" * 82)
    
    # Imprime la sección de diálogo de la ventana.
    for _ in range(altura_dialogo):
        print("|" + " " * 80 + "|")
    
    # Imprime la línea divisoria entre diálogo e interacción.
    print("-" * 82)
    
    # Imprime la sección de interacción de la ventana.
    for _ in range(altura_interaccion):
        print("|" + " " * 80 + "|")
    
    # Imprime la línea inferior de la ventana.
    print("-" * 82)
    
    return linea_actual

def obtener_mensajes_arcos(linea_actual):
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

def terminar_juego(bandera_arco, contador_arcos, nombres_arcos):
    """
    Controla el cierre del juego basado en la respuesta del usuario.
    
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

def restaurar_arco(contador_arcos, lista_avance, arco_actual, 
                   nombres_arcos, bandera_arco):
    """
    Permite al usuario regresar a un arco anterior en la historia.
    
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

def imprimir_nombre_arco(nombre_arco):
    """
    Imprime el nombre de un arco con formato especial en la consola.

    Args:
        nombre_arco (str): Nombre del arco a imprimir.

    Returns:
        None
    """
    linea = 1  # Establece la línea para posicionar el nombre del arco.
    posicionar_linea(linea)  # Posiciona la línea en la salida.

    # Formatea el nombre del arco con capitalización.
    nombre_arco = nombre_arco[:-1].capitalize() + " " + nombre_arco[-1::]
    print("| ", end="")  # Imprime el prefijo antes del nombre.

    # Imprime cada carácter del nombre del arco con un retardo.
    for caracter in nombre_arco:
        print(caracter, end="", flush=True)
        sleep(0.1)  # Retardo entre caracteres para un efecto visual.

    linea = 23  # Establece la línea para el mensaje de continuación.
    posicionar_linea(linea)  # Posiciona la línea en la salida.
    input("| Presione enter para continuar:")  # Espera a que el usuario presione Enter.

def pasar_informacion(paquete_mensajes, linea_actual, cantidad_seccion):
    """
    Procesa y muestra información de mensajes en la interfaz.

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
                                                                               lista_secciones,constante_linea, 
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

def recorrer_alternativas(alternativas, linea_actual, cantidad_seccion,
                         constante_linea, constante_rango, lista_secciones):
    """
    Procesa las alternativas seleccionadas por el usuario.

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
            constante_linea, constante_rango, lista_secciones) = imprimir_mensaje(
                linea_actual, cantidad_seccion, lista_secciones,
                constante_linea, constante_rango
            )

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

def imprimir_alternativas(alternativas):
    """
    Imprime las alternativas disponibles y solicita la selección del usuario.

    Args:
        alternativas (dict): Opciones disponibles para el usuario.

    Returns:
        tuple: Opción seleccionada por el usuario y las alternativas restantes.
    """
    LINE_UP = '\033[1A'  # Control de línea para mover el cursor hacia arriba.

    # Imprime cada alternativa con su respectiva clave y valor.
    for clave, valor in alternativas.items():
        posibilidad = "| " + clave + ") " + valor[0]  # Formato de la opción.

        # Imprime cada carácter de la opción con un retardo.
        for caracter in posibilidad:
            print(caracter, end="", flush=True)
            sleep(0.02)

    # Posiciona el cursor para las siguientes entradas del usuario.
    linea = 22
    posicionar_linea(linea)

    # Limpia el área para que el usuario pueda ver la siguiente instrucción.
    for _ in range(2):
        print("|" + " " * 70)

    print(LINE_UP, end="")  # Mueve el cursor hacia arriba.

    # Solicita la opción del usuario, normalizando la entrada.
    opcion = input("| Seleccione una opción:").lower().replace(" ", "")

    return opcion, alternativas  # Devuelve la opción y alternativas restantes.

def imprimir_imagen(archivo_imagen):
    """
    Imprime una imagen ASCII desde un archivo, caracter por caracter.

    Args:
        archivo_imagen (str): Ruta del archivo que contiene la imagen ASCII.

    Returns:
        None
    """
    linea = 1  # Posiciona el cursor en la línea 1.
    posicionar_linea(linea)

    # Abre el archivo de imagen en modo lectura.
    with open(archivo_imagen, 'r') as archivo:
        arte_ascii = archivo.read()  # Lee el contenido del archivo.

    # Imprime cada carácter de la imagen ASCII con un retardo.
    for caracter in arte_ascii:
        print(caracter, end="", flush=True)
        sleep(0.005)

    linea = 23  # Posiciona el cursor en la línea 23.
    posicionar_linea(linea)

    # Solicita al usuario que presione enter para continuar.
    input("| Presione enter para continuar:")

def posicionar_linea(linea):
    """
    Posiciona el cursor en una línea específica en la consola.

    Args:
        linea (int): Número de la línea a la que se desea mover el cursor.

    Returns:
        None
    """
    LINE_UP = '\033[1A'  # Control de línea para mover el cursor hacia arriba.

    # Mueve el cursor hacia arriba 100 veces (opcional).
    for _ in range(100):
        print(LINE_UP, end="")

    # Imprime líneas vacías hasta alcanzar la línea deseada.
    for _ in range(linea):
        print("")  # Imprime una línea vacía.

def imprimir_mensaje(linea_actual: int, cantidad_seccion: int, 
                     lista_secciones: list, constante_linea, 
                     constante_rango):
    """
    Imprime mensajes en la consola con un efecto de escritura caracter por 
    caracter. Se encarga de limpiar la pantalla y mover el cursor a la 
    posición correcta antes de imprimir cada mensaje. También actualiza 
    las variables relacionadas con la posición y el estado de la impresión.

    Args:
        linea_actual (int): Línea actual en la consola.
        cantidad_seccion (int): Cantidad de secciones impresas.
        lista_secciones (list): Lista de secciones con mensajes.
        constante_linea: Constante utilizada para controlar la línea.
        constante_rango: Rango utilizado para controlar la impresión.

    Returns:
        tuple: Línea actual, cantidad de secciones, constante de línea,
               constante de rango y lista de secciones actualizada.
    """
    # Verificar si el último mensaje está activo para impresión
    if lista_secciones[-1][0] == True:

        borrar_pantalla()  # Limpiar la pantalla para nueva impresión

        # Mover el cursor a la posición adecuada
        (linea_actual,
         cantidad_seccion, constante_linea,
         constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                          lista_secciones, constante_linea,
                                                          constante_rango)

        print("| ", end="")  # Imprimir el delimitador inicial de la línea

        # Iterar sobre cada caracter en el mensaje para imprimir
        for caracter in lista_secciones[-1][1]:
            print(caracter, end="", flush=True)
            sleep(0.02)  # Pausa breve para efecto de escritura

        borrar_pantalla()  # Limpiar la pantalla después de imprimir

        # Ajustar la línea actual y rango de mensaje después de imprimir
        (linea_actual,
         cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion,
                                                             constante_rango)

        cantidad_seccion += constante_rango  # Aumentar cantidad de secciones

        # Mover el cursor para la siguiente impresión
        (linea_actual,
         cantidad_seccion, constante_linea,
         constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                          lista_secciones, constante_linea,
                                                          constante_rango)

        print("| ", end="")  # Imprimir el delimitador de la nueva línea

        (linea_actual,
         cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion,
                                                             constante_rango)

    else:
        borrar_pantalla()  # Limpiar la pantalla si el mensaje no está activo

        # Mover el cursor a la posición adecuada
        (linea_actual,
         cantidad_seccion, constante_linea,
         constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                          lista_secciones, constante_linea,
                                                          constante_rango)

        print("|" + " " * 18, end="")  # Imprimir espacio antes del mensaje

        # Iterar sobre cada caracter en el mensaje para imprimir
        for caracter in lista_secciones[-1][1]:
            print(caracter, end="", flush=True)
            sleep(0.02)  # Pausa breve para efecto de escritura

        borrar_pantalla()  # Limpiar la pantalla después de imprimir

        # Ajustar la línea actual y rango de mensaje después de imprimir
        (linea_actual,
         cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion,
                                                             constante_rango)

        cantidad_seccion += constante_rango  # Aumentar cantidad de secciones

        # Mover el cursor para la siguiente impresión
        (linea_actual,
         cantidad_seccion, constante_linea,
         constante_rango, lista_secciones) = mover_cursor(linea_actual, cantidad_seccion,
                                                          lista_secciones, constante_linea,
                                                          constante_rango)

        (linea_actual,
         cantidad_seccion, constante_rango) = restar_linea(linea_actual, cantidad_seccion,
                                                             constante_rango)

    # Retornar la línea actual y rango de mensaje actualizados
    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def mover_cursor(linea_actual: int, cantidad_seccion: int,
                 lista_secciones: list,
                 constante_linea, constante_rango):
    """
    Mueve el cursor en la consola a la línea actual y ajusta el rango.

    Args:
        linea_actual (int): Línea actual en la consola.
        cantidad_seccion (int): Cantidad de secciones impresas.
        lista_secciones (list): Lista de secciones con mensajes.
        constante_linea: Constante utilizada para controlar la línea.
        constante_rango: Rango utilizado para controlar la impresión.

    Returns:
        tuple: Línea actual, cantidad de secciones, constante de línea,
               constante de rango y lista de secciones actualizada.
    """
    LINE_UP = '\033[1A'  # Secuencia para mover el cursor hacia arriba

    # Mover el cursor hacia arriba 100 líneas
    for _ in range(100):
        print(LINE_UP, end="")

    # Imprimir líneas vacías hasta alcanzar la línea actual
    for _ in range(linea_actual):
        # Si es la última línea y no es la 14, ajustar el rango del mensaje
        if _ == linea_actual - 1 and _ != 14:
            print("")  # Imprimir línea vacía
            cantidad_seccion, linea_actual = rango_seccion(lista_secciones, cantidad_seccion, linea_actual)

        else:
            print("")  # Imprimir línea vacía

    if _ == 0 and linea_actual == 1:
        # Verificar y ajustar la línea si es necesario
        (linea_actual, constante_linea,
         constante_rango, lista_secciones) = verificar_linea(linea_actual, constante_linea,
                                                             constante_rango, lista_secciones)

    # Devolver la línea actual y el rango de mensaje actualizados
    return linea_actual, cantidad_seccion, constante_linea, constante_rango, lista_secciones

def restar_linea(linea_actual, cantidad_seccion, constante_rango):
    """
    Ajusta la línea actual y el rango de sección según condiciones.

    Args:
        linea_actual (int): La línea actual en la consola.
        cantidad_seccion (int): La cantidad de secciones impresas.
        constante_rango: Rango utilizado para controlar la impresión.

    Returns:
        tuple: Línea actual, cantidad de secciones y constante de rango.
    """
    # Verifica si la línea actual y la cantidad de secciones son válidas
    if linea_actual != 1 and cantidad_seccion != 10:
        linea_actual -= 1  # Reduce la línea actual si es necesario

    elif linea_actual == 1 and cantidad_seccion == 7:
        linea_actual = 2  # Cambia la línea actual a 2
        constante_rango = 0  # Reinicia el rango

    # Devuelve la línea actual y el rango de sección actualizados
    return linea_actual, cantidad_seccion, constante_rango

def verificar_linea(linea_actual, constante_linea, constante_rango, lista_secciones):
    """
    Verifica y ajusta los parámetros de línea y sección.

    Args:
        linea_actual (int): La línea actual en la consola.
        constante_linea: Valor que representa la línea constante.
        constante_rango: Valor que representa el rango constante.
        lista_secciones (list): Lista de secciones disponibles.

    Returns:
        tuple: Línea actual, constante de línea, constante de rango y lista de secciones.
    """
    constante_linea = 0  # Reinicia la constante de línea
    constante_rango = 0  # Reinicia la constante de rango

    lista_secciones.pop(0)  # Elimina la primera sección de la lista

    # Devuelve los parámetros actualizados
    return linea_actual, constante_linea, constante_rango, lista_secciones

def rango_seccion(lista_secciones: list, cantidad_seccion: int, linea_actual):
    """
    Ajusta el rango de secciones a mostrar en la interfaz.

    Args:
        lista_secciones (list): Lista de secciones disponibles.
        cantidad_seccion (int): Número de secciones a mostrar.
        linea_actual: La línea actual en la consola.

    Returns:
        tuple: Cantidad de secciones y línea actual.
    """
    i = 0         # Inicializa el índice de la línea actual
    seccion = 0   # Inicializa el índice de la sección actual

    # Bucle para ajustar el rango de secciones a mostrar
    while i < cantidad_seccion:
        # Llama a imprimir_seccion para mostrar la sección actual
        seccion, i, lista_secciones = imprimir_seccion(lista_secciones, seccion, i)

        # Actualiza los índices para la próxima sección
        seccion += 1
        i += 1

    # Retorna la cantidad de secciones y la línea actual
    return cantidad_seccion, linea_actual

def imprimir_seccion(lista_secciones: list, seccion: int, i: int):
    """
    Imprime una sección del mensaje según su estado activo.

    Args:
        lista_secciones (list): Lista de secciones con sus estados.
        seccion (int): Índice de la sección a imprimir.
        i (int): Índice actual del bucle.

    Returns:
        tuple: Índice de la sección, índice actual y lista de secciones.
    """
    # Imprimir el mensaje según el estado activo de la sección
    if lista_secciones[seccion][0] == True:
        print("| " + lista_secciones[seccion][1])
    else:
        # Imprimir espacio en blanco si la sección no está activa
        print("| " + " " * 18 + lista_secciones[seccion][1])

    # Devolver los valores actualizados
    return seccion, i, lista_secciones

def borrar_pantalla():
    """
    Borra el contenido de la pantalla desplazando el cursor hacia arriba.

    Args:
        None

    Returns:
        None
    """
    LINE_UP = '\033[1A'  # Secuencia de escape ANSI para mover el cursor arriba

    # Mover el cursor hacia arriba 100 líneas para limpiar la pantalla
    for _ in range(100):
        print(LINE_UP, end="")

    print("")  # Imprimir una línea en blanco para separar el contenido

    # Imprimir líneas vacías para simular el borrado de la pantalla
    for _ in range(15):
        print("|" + " " * 80)

if __name__ == "__main__":

    # Limpiar la pantalla para una mejor visualización
    os.system('cls')

    # Obtener la línea actual para imprimir la ventana
    linea_actual = imprimir_ventana()

    # Cargar y mostrar los mensajes de los arcos
    obtener_mensajes_arcos(linea_actual)
