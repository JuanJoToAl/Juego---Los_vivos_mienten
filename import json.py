import json

with open('dialogos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for escena, contenido in data.items():
    print(contenido["dialogo"])
    for opcion in contenido["opciones"]:
        print(opcion)
