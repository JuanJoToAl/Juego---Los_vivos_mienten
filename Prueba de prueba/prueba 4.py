#Quiero que en una variable quede la orientación y el mensaje seccionado
# Arreglar lo que está pasando con el if y elif cuando quito el elif y quito el and
import os
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
#fasfafasdasda
def dividir_mensaje(lista_mensajes: list, ancho_pantalla: int, 
                    sublista : int, seccion_escritura : list):
    mensaje = lista_mensajes[sublista][1]
    lista_mensajes[sublista].remove(lista_mensajes[sublista][1])
    seccion_escritura = []
    ancho_texto = ancho_pantalla - 20
    recorrido = 0
    contador = 0
    bandera = True

    while recorrido < len(mensaje) and bandera:
        if mensaje[contador] == " " and contador < ancho_texto:
            indice = contador
        elif ancho_texto <= contador:
            seccion_escritura.append(mensaje[:indice])
            mensaje = mensaje[indice:].lstrip()  
            recorrido = 0
            contador = 0
        elif len(mensaje) < ancho_texto:
            seccion_escritura.append(mensaje)
            bandera = False
        
        recorrido += 1
        contador += 1

    lista_mensajes[sublista].append(seccion_escritura)

    return seccion_escritura, lista_mensajes

def imprimir_mensaje(seccion_escritura, lista_mensajes : list, linea_actual, 
                     ancho_pantalla : int, sublista : int, rango_mensaje: int):
    
    if lista_mensajes[sublista][0] == True:
        # Imprimir cada carácter con el efecto de escritura
        linea_actual, rango_mensaje,  = mover_cursor(linea_actual, rango_mensaje, lista_mensajes)
        print("| ", end = "")

        for palabra in seccion_escritura:
            
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)
            
            borrar_pantalla(ancho_pantalla)

            linea_actual -= 1
            rango_mensaje -=1

            linea_actual, rango_mensaje,  = mover_cursor(linea_actual, rango_mensaje, lista_mensajes)
            print("| ", end = "")

            
    else:
        borrar_pantalla(ancho_pantalla)
        linea_actual -= 1
        
        linea_actual, rango_mensaje,  = mover_cursor(linea_actual, rango_mensaje, lista_mensajes)
        print('\n', end = "")
        for palabra in seccion_escritura:  
            print("|" + " " * 18, end = "")
            for caracter in palabra:
                print(caracter, end="", flush=True)
                sleep(0.02)

            borrar_pantalla(ancho_pantalla)

            linea_actual -= 1
            rango_mensaje -=1

            linea_actual, rango_mensaje,  = mover_cursor(linea_actual, rango_mensaje, lista_mensajes)
           
    return linea_actual, rango_mensaje



def mover_cursor(linea_actual, rango_mensaje, lista_mensajes):

    #Codigo ANSI para subir de linea
    LINE_UP = '\033[1A'

    #Poner el cursor arriba del todo
    for _ in range(100):
        print(LINE_UP, end="")

    for _ in range(linea_actual):
        if _ == linea_actual - 1 and _ != 14:
            print("")
            rango_mensaje, contador, frase = rango_seccion(lista_mensajes, rango_mensaje)
        else:
            print("")
        
    return linea_actual, rango_mensaje

def rango_seccion(lista_mensajes, rango_mensaje):
    contador = 0
    frase = 0
    i = 0
    seccion = 0
    
    while i < 15 - rango_mensaje:
        if seccion < len(lista_mensajes[contador][1]):
            frase, seccion, i, contador, lista_mensajes = imprimir_seccion(lista_mensajes, contador, 
                                                                           frase, seccion, i)
        else:
            print("| " + " " * 18)
            contador +=1
            frase = 0
            seccion = 0
    
    return rango_mensaje, contador, frase

def imprimir_seccion(lista_mensajes, contador, frase, seccion, i):
    if lista_mensajes[contador][0] == True:
        print("| " + lista_mensajes[contador][1][frase])

    else:
        print("| " + " " * 18 + lista_mensajes[contador][1][frase])

    frase += 1
    seccion += 1
    i += 1

    return frase, seccion, i, contador, lista_mensajes

def borrar_pantalla(ancho_pantalla):
    LINE_UP = '\033[1A'
    for _ in range(100):
        print(LINE_UP, end = "")

    print("")

    for _ in range(15):
        print("|" + " " * ancho_pantalla)

if __name__ == "__main__":

    ancho_pantalla = 80
    altura_dialogo = 15
    altura_interaccion = 8
    linea_actual = deepcopy(altura_dialogo) 
    rango_mensaje = deepcopy(linea_actual)
    os.system('cls')

    imprimir_ventana(ancho_pantalla, altura_dialogo, altura_interaccion)

    lista_mensajes = [[True, "[Serpiente]: Muchos años después, frente al pelotón de fusilamiento, el "
               "coronel Aureliano Buendía había de recordar aquella tarde remota en que "
               "su padre lo llevó a conocer el hielo."], [False, "[Serpiente]: La tierra, recién salida del barro, olía a hierba húmeda. Aureliano Buendía sintió el frío de la madrugada y se arrepintió de haber abandonado el sueño. Pero Úrsula, que era más práctica, le ordenó que fuera a reconocer los límites de la propiedad. Aureliano Buendía salió a galope, con las espuelas clavadas en los flancos del caballo, y regresó a mediodía con los ojos enrojecidos por el sol, la ropa hecha jirones y la frente surcada de sudor. Traía consigo la certeza de que habían llegado al fin del mundo."]]
    
    sublista = 0
    seccion_escritura = []

    seccion_escritura, lista_mensajes = dividir_mensaje(lista_mensajes, ancho_pantalla, sublista, 
                                                                         seccion_escritura)
    linea_actual, rango_mensaje = imprimir_mensaje(seccion_escritura, lista_mensajes, linea_actual, 
                                    ancho_pantalla, sublista, rango_mensaje)
    
    #mensaje = 
    #lista_mensajes.append(mensaje)
    sublista += 1
    seccion_escritura, lista_mensajes = dividir_mensaje(lista_mensajes, ancho_pantalla, sublista, 
                                                                         seccion_escritura)
    linea_actual, rango_mensaje = imprimir_mensaje(seccion_escritura, lista_mensajes, linea_actual, 
                                                   ancho_pantalla, sublista, rango_mensaje)
    



