#En este código cuando la sección mensaje entra en el else de imprimir mensaje
#está llena con las secciones del primer texto y del segundo texto

from time import sleep
from copy import deepcopy

def screener(ancho_pantalla, height1, altura_interaccion):
    print("-" * (ancho_pantalla + 2))
    for _ in range(height1):
        print("|" + " " * ancho_pantalla + "|")
    print("-" * (ancho_pantalla + 2))
    for _ in range(altura_interaccion):
        print("|" + " " * ancho_pantalla + "|")
    print("-" * (ancho_pantalla + 2))

def dividir_mensaje(lista_mensajes: list, ancho_pantalla: int, 
                    sublista : int, seccion_mensaje : list):
    repuesto_lista_mensaje = deepcopy(lista_mensajes)
    ancho_texto = ancho_pantalla - 20
    recorrido = 0
    contador = 0
    bandera = True

    while recorrido < len(lista_mensajes[sublista][1]) and bandera:
        if lista_mensajes[sublista][1][contador] == " " and contador < ancho_texto:
            indice = contador
        elif ancho_texto <= contador:
            seccion_mensaje.append(lista_mensajes[sublista][1][:indice])
            lista_mensajes[sublista][1] = lista_mensajes[sublista][1][indice:].lstrip()  
            recorrido = 0
            contador = 0
        elif len(lista_mensajes[sublista][1]) < ancho_texto:
            seccion_mensaje.append(lista_mensajes[sublista][1])
            bandera = False
        
        recorrido += 1
        contador += 1

    lista_mensajes = repuesto_lista_mensaje
    
    return seccion_mensaje, lista_mensajes

def imprimir_mensaje(seccion_mensaje, lista_mensajes : list, 
                     linea_actual, ancho_pantalla : int):
    #print(f"Valor línea actual antes de ciclo:{linea_actual}")
    if lista_mensajes[sublista][0] == "derch":
        # Imprimir cada carácter con el efecto de escritura
        linea_actual = mover_cursor(linea_actual, lista_mensajes, 
                                              seccion_mensaje)
        print("| ", end = "")

        for palabra in seccion_mensaje:
            
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)
            
            borrar_pantalla(ancho_pantalla)
            linea_actual -= 1
            linea_actual = mover_cursor(linea_actual, lista_mensajes, 
                                        seccion_mensaje)
            print("| ", end = "")
            #print(f"Valor línea actual en ciclo:{linea_actual}")
            
    else:
        borrar_pantalla(ancho_pantalla)
        linea_actual = mover_cursor(linea_actual, lista_mensajes, 
                                    seccion_mensaje)
        print(f"sección mensaje actual:{seccion_mensaje}")

        #for palabra in seccion_mensaje:  
         #   for caracter in palabra:
          #      print(caracter, end="", flush=True)
           #     sleep(0.02)
           # print('\n' + "|" + " " * 18, end = "")
           # linea_actual -= 1

    return linea_actual
            
def mover_cursor(linea_actual, lista_mensajes, 
                 seccion_mensaje):

    #Codigo ANSI para subir de linea
    LINE_UP = '\033[1A'

    #Poner el cursor arriba del todo
    for _ in range(100):
        print(LINE_UP, end="")

    for _ in range(linea_actual):
        if _ == linea_actual - 1 and _ != 15:
            print("")
            imprimir_seccion(lista_mensajes, linea_actual, 
                                        seccion_mensaje)
        else:
            print("")
        
    return linea_actual

def imprimir_seccion(lista_mensajes, linea_actual, 
                     seccion_mensaje):
    #print(f"La línea actual es:{linea_actual}")
    #print(f"sección mensaje es:{seccion_mensaje}")
    #print(f"lista mensajes es:{lista_mensajes}")
    marcador = 0
    if lista_mensajes[marcador][0] == "derch":
        
        for i in range(16 - linea_actual):
            print("| " + seccion_mensaje[i])
        marcador += 1
    else:
        print("entrada", "g" * 20)
        for i in range(16 - linea_actual):
            print("| " + " " * 18 + seccion_mensaje[i])
            #print(f"Lo que se está accediendo: {lista_mensajes[sublista][1]}")
        marcador += 1

def borrar_pantalla(ancho_pantalla):
    LINE_UP = '\033[1A'
    for _ in range(100):
        print(LINE_UP, end = "")

    print("")
    print("")

    for _ in range(15):
        print("|" + " " * ancho_pantalla)

if __name__ == "__main__":

    ancho_pantalla = 80
    altura_dialogo = 15
    altura_interaccion = 8
    linea_actual = altura_dialogo + 1

    screener(ancho_pantalla, altura_dialogo, altura_interaccion)

    lista_mensajes = []
    mensaje = ["derch", "[Serpiente]: Muchos años después, frente al pelotón de fusilamiento, el "
               "coronel Aureliano Buendía había de recordar aquella tarde remota en que "
               "su padre lo llevó a conocer el hielo."]
    lista_mensajes.append(mensaje)
    
    sublista = 0
    seccion_mensaje = []

    seccion_mensaje, lista_mensajes = dividir_mensaje(lista_mensajes, ancho_pantalla, 
                                                      sublista, seccion_mensaje)
    linea_actual = imprimir_mensaje(seccion_mensaje, lista_mensajes, 
                                    linea_actual, ancho_pantalla)
    
    
    mensaje = ["izqrd", "[Serpiente]: La tierra, recién salida del barro, olía a hierba húmeda. Aureliano Buendía sintió el frío de la madrugada y se arrepintió de haber abandonado el sueño. Pero Úrsula, que era más práctica, le ordenó que fuera a reconocer los límites de la propiedad. Aureliano Buendía salió a galope, con las espuelas clavadas en los flancos del caballo, y regresó a mediodía con los ojos enrojecidos por el sol, la ropa hecha jirones y la frente surcada de sudor. Traía consigo la certeza de que habían llegado al fin del mundo."]
    lista_mensajes.append(mensaje)
    sublista += 1
    seccion_mensaje, lista_mensajes = dividir_mensaje(lista_mensajes, ancho_pantalla, 
                                                      sublista, seccion_mensaje)
    linea_actual = imprimir_mensaje(seccion_mensaje, lista_mensajes, 
                                    linea_actual, ancho_pantalla)
