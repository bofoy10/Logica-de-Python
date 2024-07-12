print("""
    +================+
    |                |
    |      JSON      |
    |                |
    +================+ 
          """)


# leer el json 
import json 

# abrir el archivo .json
with open('datos.json','r') as file:
    datos = json.load(file)

print(datos)


# escribir dentro del json
datos = { 
    "nombre":"pepito",
    "edad":15,
    "ciudad":"santiago"
}
# escrivir en el jason
with open('datos.json','w') as file:
    json.dump(datos, file)



# actualizar el json (primero se abre el archivo)
with open('datos.json', 'r') as file:
    datos = json.load.file(json)

# Actualizar
datos['edad'] = 31
# escrivir de vuelta el json
with open('datos.json', 'w') as file:
    datos = json.dump(datos, file)


# buscar en un json
with open('datos.json', 'r') as file:
    datos = json.load.file(json)

print(datos['nombre'])
# en teoria imprimira juan

#verificar si existe una clave 
if 'ciudad' in datos:
    print(datos['ciudad']) #en teoria impimira santiago


# borrar json 
with open('datos.json', 'r') as file:
    datos = json.load.file(json)

# borrar una dato u clave
if 'edad' in datos:
    del datos['edad']

#escrivir de vuelta el json
with open('datos.json', 'r') as file:
    datos = json.dump(datos, file)