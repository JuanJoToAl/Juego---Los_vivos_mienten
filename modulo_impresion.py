from copy import deepcopy  # Importa deepcopy para copiar objetos complejos
from time import sleep  # Importa la función sleep para pausas en el tiempo

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

def posicionar_linea(linea: int) -> None:
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

def imprimir_nombre_arco(nombre_arco: str) -> None:
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

def imprimir_alternativas(alternativas: dict) -> tuple:
    """
    Imprime las opciones disponibles con un efecto de escritura animada 
    y solicita al usuario que seleccione una de ellas.

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

def imprimir_imagen(archivo_imagen: str) -> None:
    """
    Imprime una imagen ASCII desde un archivo, carácter por carácter, con 
    un efecto de escritura progresiva. 

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

def imprimir_mensaje(linea_actual: int, cantidad_seccion: int, 
                     lista_secciones: list, constante_linea: int, 
                     constante_rango: int) -> tuple:
    """              
    Imprime mensajes en la consola con un efecto de escritura caracter por 
    caracter. Se encarga de hacer el control de cuando limpiar la pantalla y
    mover el cursor a la posición correcta antes de imprimir cada mensaje.
    También actualiza las variables relacionadas con la posición y el estado de
    la impresión.
    
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

def mover_cursor(linea_actual: int, 
                 cantidad_seccion: int, lista_secciones: list, 
                 constante_linea: int, constante_rango: int) -> tuple:
    """          
    Mueve el cursor de la consola a la posición de la línea deseada y ajusta 
    el rango de impresión de mensajes. También verifica y ajusta las variables
    relacionadas con el control de la impresión en función de la línea y
    sección actuales.
    
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

def restar_linea(linea_actual: int, 
                 cantidad_seccion: int, constante_rango: int) -> tuple:
    """
    Ajusta la posición de la línea y el rango de sección para el texto. Además,
    maneja las condiciones de retroceso de línea y reinicio de rango.

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

def verificar_linea(linea_actual: int, constante_linea: int, 
                    constante_rango: int, lista_secciones: list) -> tuple:
    """
    Ajusta las constantes de línea y rango a cero, eliminando la primera
    sección de la lista para avanzar en la narrativa.

    Args:
        linea_actual (int): La línea actual en la consola.
        constante_linea: Valor que representa la línea constante.
        constante_rango: Valor que representa el rango constante.
        lista_secciones (list): Lista de secciones disponibles.

    Returns:
        tuple: Línea actual, constante de línea, constante de rango y lista de
        secciones.        
    """
    constante_linea = 0  # Reinicia la constante de línea
    constante_rango = 0  # Reinicia la constante de rango

    lista_secciones.pop(0)  # Elimina la primera sección de la lista

    # Devuelve los parámetros actualizados
    return linea_actual, constante_linea, constante_rango, lista_secciones

def rango_seccion(lista_secciones: list, 
                  cantidad_seccion: int, linea_actual: int) -> tuple:
    """
    Muestra un rango de secciones en la interfaz, ajustando el índice según sea
    necesario.
    
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

def imprimir_seccion(lista_secciones: list, 
                     seccion: int, i: int) -> tuple:
    """
    Muestra el mensaje de la sección si está activa o deja un espacio en
    blanco si no lo está.

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

def borrar_pantalla() -> None:
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
