import gui
import dialoguito
from dialoguito import add_message, write_all_messages
from time import sleep

#Limpiar todo lo que está previamente escrito en consola
import os
os.system('cls')

#Definir el tamaño de la ventana
window_width = 80
window_height1 = 15
window_height2 = 8

#Crear los bordes del juego
gui.screener(window_width, window_height1, window_height2)

sleep(1)
add_message("ext", "Serpiente", "Acaso, eres el cobrador de impuestos, porque sin duda me arrastraria hacia ti")
sleep(1)
add_message("int", "Ángela", "Esto es un mensaje muuuuuuuuuuy largo de prueba, vamos a ver que sucede. Creo que estoy entendiendo")
sleep(1)
add_message("int", "Ángela", "Denme unos minutos...")
sleep(1)
add_message("ext", "Fabian", "Estaba esperando qué decías Jajajaja. Nueva prueba para ver qué sucede")
sleep(1)
add_message("ext", "Fabian", "Salchipapas :3")
sleep(1)
add_message("int", "Ángela", "Listo, vali chota pero listo, donde se le hace, y que se le hace?")
sleep(1)
add_message("ext", "Mariana", "al final entre quiénes lo vamos a hacer")
sleep(1)
add_message("ext", "Mariana", "El jabón favorito tiene discord?")



while True:
    pass
#to