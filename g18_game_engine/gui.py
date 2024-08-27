#Crea los bordes del juego con un ancho y altos definidos
def screener(width, height1, height2):
    print("-" * (width + 2))
    for _ in range(height1):
        print("|" + " " * width + "|")
    print("-" * (width + 2))
    for _ in range(height2):
        print("|" + " " * width + "|")
    print("-" * (width + 2))

#Posiciona el cursor en una linea específica para poder sobreescribir lineas
def change_cursor_position(position):
    #Codigo ANSI para subir de linea
    LINE_UP = '\033[1A'

    #Poner el cursor arriba del todo
    for _ in range(100):
        print(LINE_UP, end="")

    for _ in range(position):
        print()