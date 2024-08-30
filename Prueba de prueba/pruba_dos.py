# Código más completo hasta ahora
#Revizar qué está pasando con linea_actual y poner condicional en imprimir
#seccion, creo que va a tocar usar la variable lista_mensajes en vez de
#seccion_escritura

#Imprime el primer texto otra vez con la animación de escritura y alineado a la derecha

from time import sleep
from copy import deepcopy

def imprimir_ventana(ancho_pantalla, height1, altura_interaccion):
    print("-" * (ancho_pantalla + 2))
    for _ in range(height1):
        print("|" + " " * ancho_pantalla + "|")
    print("-" * (ancho_pantalla + 2))
    for _ in range(altura_interaccion):
        print("|" + " " * ancho_pantalla + "|")
    print("-" * (ancho_pantalla + 2))

def dividir_mensaje(lista_mensajes: list, ancho_pantalla: int, 
                    sublista : int, seccion_escritura : list, seccion_mensaje : list):
    repuesto_lista_mensaje = deepcopy(lista_mensajes)
    seccion_escritura = []
    ancho_texto = ancho_pantalla - 20
    recorrido = 0
    contador = 0
    bandera = True

    while recorrido < len(lista_mensajes[sublista][1]) and bandera:
        if lista_mensajes[sublista][1][contador] == " " and contador < ancho_texto:
            indice = contador
        elif ancho_texto <= contador:
            seccion_escritura.append(lista_mensajes[sublista][1][:indice])
            lista_mensajes[sublista][1] = lista_mensajes[sublista][1][indice:].lstrip()  
            recorrido = 0
            contador = 0
        elif len(lista_mensajes[sublista][1]) < ancho_texto:
            seccion_escritura.append(lista_mensajes[sublista][1])
            bandera = False
        
        recorrido += 1
        contador += 1

    lista_mensajes = repuesto_lista_mensaje
    seccion_mensaje += seccion_escritura
    print(seccion_mensaje)
    return seccion_escritura, lista_mensajes, seccion_mensaje

def imprimir_mensaje(seccion_escritura, lista_mensajes : list, linea_actual, 
                     ancho_pantalla : int, sublista : int, rango_mensaje: int):
    #print(f"Valor línea actual antes de ciclo:{linea_actual}")
    if lista_mensajes[sublista][0] == "derch":
        # Imprimir cada carácter con el efecto de escritura
        linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje, 
                                                   lista_mensajes, seccion_mensaje)
        print("| ", end = "")

        for palabra in seccion_escritura:
            
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)
            
            borrar_pantalla(ancho_pantalla)

            linea_actual -= 1
            rango_mensaje -=1

            linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje, 
                                                       lista_mensajes, seccion_mensaje)
            print("| ", end = "")
            #print(f"Valor línea actual en ciclo:{linea_actual}")
            
    else:
        borrar_pantalla(ancho_pantalla)
        linea_actual -= 1
        
        #print("h" * 80 , linea_actual)
        linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje, 
                                                   lista_mensajes, seccion_mensaje)

        for palabra in seccion_escritura:  
            print('\n' + "|" + " " * 18, end = "")
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)

            borrar_pantalla(ancho_pantalla)

            linea_actual -= 1
            rango_mensaje -=1

            linea_actual, rango_mensaje = mover_cursor(linea_actual, rango_mensaje, 
                                                        lista_mensajes, seccion_mensaje)
            

    #print("h" * 80, linea_actual)

    #linea_actual -= 1

    return linea_actual, rango_mensaje
            
def mover_cursor(linea_actual, rango_mensaje, 
                 lista_mensajes, seccion_mensaje):

    #Codigo ANSI para subir de linea
    LINE_UP = '\033[1A'

    #Poner el cursor arriba del todo
    for _ in range(100):
        print(LINE_UP, end="")

    for _ in range(linea_actual):
        if _ == linea_actual - 1 and _ != 15:
            print("")
            rango_mensaje = imprimir_seccion(lista_mensajes, rango_mensaje, 
                                            seccion_mensaje)
        else:
            print("")
        
    return linea_actual, rango_mensaje

def imprimir_seccion(lista_mensajes, rango_mensaje, 
                     seccion_mensaje):
    marcador = 0
    if lista_mensajes[marcador][0] == "derch":
        print(f"Rango de mensajes:{16 - rango_mensaje}")
        for i in range(16 - rango_mensaje):
            print("| " + seccion_mensaje[i])
        marcador += 1
        #print(f"esteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee es el marcador:{marcador}")
    else:
        #print("entradaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        for i in range(16 - rango_mensaje):
            print("| " + " " * 18 + seccion_mensaje[i])
            #print(f"Lo que se está accediendo: {lista_mensajes[sublista][1]}")
        marcador += 1
    
    return rango_mensaje

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
    rango_mensaje = deepcopy(linea_actual)

    imprimir_ventana(ancho_pantalla, altura_dialogo, altura_interaccion)

    lista_mensajes = [["derch", "[Serpiente]: Muchos años después, frente al pelotón de fusilamiento, el "
               "coronel Aureliano Buendía había de recordar aquella tarde remota en que "
               "su padre lo llevó a conocer el hielo."]]
    
    sublista = 0
    seccion_escritura = []
    seccion_mensaje = []

    seccion_escritura, lista_mensajes, seccion_mensaje = dividir_mensaje(lista_mensajes, ancho_pantalla, sublista, 
                                                                         seccion_escritura, seccion_mensaje)
    linea_actual, rango_mensaje = imprimir_mensaje(seccion_escritura, lista_mensajes, linea_actual, 
                                    ancho_pantalla, sublista, rango_mensaje)
    
    
    mensaje = ["izqrd", "[Serpiente]: La tierra, recién salida del barro, olía a hierba húmeda. Aureliano Buendía sintió el frío de la madrugada y se arrepintió de haber abandonado el sueño. Pero Úrsula, que era más práctica, le ordenó que fuera a reconocer los límites de la propiedad. Aureliano Buendía salió a galope, con las espuelas clavadas en los flancos del caballo, y regresó a mediodía con los ojos enrojecidos por el sol, la ropa hecha jirones y la frente surcada de sudor. Traía consigo la certeza de que habían llegado al fin del mundo."]
    lista_mensajes.append(mensaje)
    sublista += 1
    seccion_escritura, lista_mensajes, seccion_mensaje = dividir_mensaje(lista_mensajes, ancho_pantalla, sublista, 
                                                                         seccion_escritura, seccion_mensaje)
    linea_actual, rango_mensaje = imprimir_mensaje(seccion_escritura, lista_mensajes, linea_actual, 
                                                   ancho_pantalla, sublista, rango_mensaje)
