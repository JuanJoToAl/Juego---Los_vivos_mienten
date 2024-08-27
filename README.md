# Índice

1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Contribución](#contribución)
5. [Licencia](#licencia)
6. [Contacto](#contacto)

## Introducción

Aquí va una breve descripción del proyecto.

## Instalación

Instrucciones para instalar y configurar el proyecto.

## Uso

Cómo utilizar el proyecto una vez instalado.

## Contribución

Cómo puedes contribuir al proyecto.

## Licencia

Información sobre la licencia del proyecto.

## Contacto

Cómo contactar con los desarrolladores o responsables del proyecto.

# Proyecto programación

## Pseudocódigo
La siguiente sección contiene el diagrama de flujo del juego. Se empieza con una estrucutar general y seguida de esta las explicaciones específicas
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

### Función imprimir_mensaje
```mermaid
flowchart TD
    A[[imprimir_mensaje]]
```
Esta función se encarga de imprimir los mensajes ya rebanados en frases, esto con la ilusión de que se están escribiendo las palabra por teclado.
El criterio para dividir los mensajes en frases es la longitud de las frases establecida por la variable ancho_texto.


### Función imprimir_animacion
```mermaid
flowchart TD
    A[[imprimir_animacio]]
```
Esta función se encarga de las animaciones que acompañan algunos diálogos de los arcos de la historia. Esto se hace utilizando caracteres ASCII.
