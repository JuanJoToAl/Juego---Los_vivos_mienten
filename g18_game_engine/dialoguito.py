import gui
from time import sleep

#Definir el tamaño de la ventana
window_width = 80
window_height1 = 15
window_height2 = 8

chat_list = [(None, None, None)] * 10
#chat_list, lista de mensajes, cada mensaje esta guardado como una tupla (type, remitente, msg)
#type puede ser ("tht", "ext", "int")

#Devuelve un array con el string original dividido de forma que cada linea no supere el width seleccionado, también agrega una linea vacia al inicio
def slice_message(width, message):
    sliced_message = [""]

    #A place to temporalily save each line
    message_slice = ""

    #Split the message in words
    all_words = message.split()
    for word in all_words:
        #Check if we can add the word in the temporary line, or should we add it to a new line
        if len(message_slice) + len(word) > width:
            sliced_message.append(message_slice)
            message_slice = ""
        message_slice += word + " "
    sliced_message.append(message_slice)
    return sliced_message

def write_all_messages():
    current_line = window_height1 - 1
    writing_ended = False

    for type, remitente, msg in chat_list:
        if writing_ended:
            break
        if msg == None:
            continue
        #Add the remitent if needed"
        if type == "ext" or type == "int":
            pre_message = "[" + remitente + "] "
        msg = pre_message + msg
        #Break the message in lines
        broken_message = slice_message(window_width - 20, msg)
        
        #Add all lines from bottom to top
        for i in range(len(broken_message) - 1, -1, -1):
            #Jump the cursor to where we should write
            gui.change_cursor_position(current_line + 1)
            message = ""

            #Aesthetic: 2nd line and after have an extra space
            if i == 1:
                print("| ", end = "")
            else:
                print("|  ", end = "")

            #Justify the message to the left
            if type == "ext":
                print(broken_message[i].ljust(window_width - 2))
            #Justify the message to the right
            if type == "int":
                print(" " * 18 + broken_message[i].ljust(window_width - 21))
            current_line -= 1
            #If we reached the writing limit, don't write anymore
            if current_line < 0:
                writing_ended = True
                break
            


def add_message(type, remitente, msg):
    #Agrega el nuevo mensaje al inicio, y elimina el ultimo mensaje
    chat_list.insert(0, (type, remitente, ""))
    del chat_list[10]
    #Add the message gradually, to make the animation
    for i in range(len(msg)):
        chat_list[0] = (type, remitente, msg[:i + 1])
        if msg[i] != " ":
            sleep(0.05)
        write_all_messages()
    