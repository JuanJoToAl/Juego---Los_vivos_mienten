# Proyecto programación
# Índice
1. [Pseudocódigo](#pseudocódigo)
    1. [Estructuar general del juego](#estructuar-general-del-juego)
    2. [Función imprimir_mensaje](#función-imprimir_mensaje)
    3. [Función imprimir_animacion](#función-imprimir_animacion)
    4. [Estructura mecánicas del juego](#estructura-mecanicas-del-juego)
    5. [Función taxi](#función-taxi)
    6. [Función diario](#función-diario)

## Pseudocódigo
La siguiente sección contiene el diagrama de flujo del juego. Se empieza con una estrucutar general y seguida de esta se presentan las explicaciones específicas
### Estructuar general del juego
```mermaid
flowchart TD
    A(Inicio) --> B
    B[ancho_pantalla = 80] -->C[altura_dialogo = 15]
    C --> D[altura_interaccion = 8]
    D --> E[ancho_texto = ancho_pantalla - 20]
    E --> F[["Se imprime la ventana de juego con la función 'imprimir_ventana'"]]
    F --> G{¿Hay arcos disponibles?}
    G -- Sí --> H{¿Hay mensajes por imprimir en el arco?}
        H -- Sí --> I["mensaje = [alineación del mensaje, texto]"]
            I --> J[["Se divide el mensaje con función 'dividir_mensaje'"]]
            J --> K[["Se imprime el mensaje con función 'imprimir_mensaje'"]]
            K --> L{¿Hay animaciones por imprimir?}
                L -- Sí --> M[["Se imprime la animación con función 'imprimir_animación'"]]
                    M --> N{¿Hay opciones de diálogo por imprimir?}
                    N -- Sí --> O["opcion_dialogo = [alineación del mensaje, texto]"]
                        O --> P[["Se divide el mensaje con función 'dividir_mensaje'"]]
                        P --> Q[["Se imprime el mensaje con función 'imprimir_mensaje'"]]
                        Q --> H
                    N -- NO --> H
                L -- No --> N
        H -- No --> G
    G -- No --> R(Fin)
```
### Función imprimir_ventana
```mermaid
flowchart TD
    A[[Imprimir_ventana]]
```
La función imprimir_ventana se encarga de imprimir la ventana de juego con unas dimensiones establecidas.

### Función dividir_mensaje
```mermaid
flowchart TD
    A[[dividir_mensaje]]
```
La función dividir_mensaje se encarga de tomar el mensaje y dividirlo de tal manera que quepa en el ancho de la pantalla. Si no cabe, hace nuevos renglones.

### Función imprimir_mensaje
```mermaid
flowchart TD
    A[[imprimir_mensaje]]
```
La función imprimir_mensaje se encarga de imprimir los mensajes ya rebanados en frases y con la ilusión de que se están escribiendo las palabras por teclado.
El criterio para dividir los mensajes en frases es la longitud de las frases establecida por la variable ancho_texto.


### Función imprimir_animacion
```mermaid

flowchart TD
    A[[imprimir_animacion]]
```
La función imprimir_animacion se encarga de imprimir las animaciones que acompañan algunos diálogos de los arcos de la historia. Estas se crean utilizando caracteres ASCII.

### Estructura mecánicas del juego
Los siguientes pseudocódigos muestran la estructura de las funciones del juego como tal.

Este primer pseudocódigo representa cada vez que el jugador decide usar el taxi.
```mermaid

flowchart TD
    n2("Inicio") --> n3{"¿Utilizar mochila?"}
    n3 -- No --> n4["Fin"]
    n3 -- Si --> n5["Escoger una opción:<br>a) Dinero<br>b) Cartera<br>c) Bolígrafo<br>d) Lupa<br>e) Diario"]
    n5 --> n6{"¿La opción seleccionada es a?"}
    n6 -- No --> n7["(Diálogo) -No creo que pueda pagar con esto"]
    n6 -- Si --> n8[["taxi"]]
    n7 --> n6
    n8 --> n9{"¿Bajarse del taxi?"}
    n9 -- No --> n10["(Diálogo) -Ya me pago señor, puede bajarse"]
    n9 -- Si --> n11["Continuar el juego"]
    n10 --> n9
```
### Función taxi
```mermaid
flowchart TD
    A[[taxi]]
```
La función taxi se encarga de tomar el entero que representa el dinero del jugador, y le resta el valor de la carrera de taxi.

Este segundo pseudocódigo respresenta cada vez que al jugador se le da la opción de usar el inventario en medio de la historia.
```mermaid
flowchart TD
    n2("Inicio") --> n3{"¿Utilizar mochila?"}
    n3 -- No --> n4["Fin"]
    n3 -- Si --> n5["Escoger una opción:<br>a) Dinero<br>b) Cartera<br>c) Bolígrafo<br>d) Lupa<br>e) Diario"]
    n5 --> n6{"¿La opción seleccionada es a o b?"}
    n6 -- Si --> n7["(Diálogo) -No creo que pueda usar esto"]
    n6 -- No --> n8{"¿La opción seleccionada es c?<br>"}
    n8 -- Si --> n9["Usar en:<br>a) Cartas (o pruebas)<br>b) Diario"]
    n8 -- No --> n10{"¿La opción seleccionada es d?"}
    n7 --> n5
    n9 --> n11{"¿La opción seleccionada es a?"}
    n11 -- Si --> n12["(Diálogo) -No puedo comprometer las pruebas"]
    n13[["Diario"]] --> n14["Continuar el juego"]
    n10 -- Si --> n15[["Lupa"]]
    n10 -- No --> n16{"¿La opción seleccionada es e?"}
    n12 --> n9
    n15 --> n14
    n11 --> n13
    n16 -- Si --> n13
    n16 -- No --> n17["Por favor, elija una opción"]
    n17 --> n5


```

### Función diario
```mermaid
flowchart TD
    A[[diario]]
```
Es una función que se encarga de modificar el diario, que es una lista la cual guarda el texto que el jugador quiera, estas notas se pueden editar, borra o se pueden escribir unas nuevas.
