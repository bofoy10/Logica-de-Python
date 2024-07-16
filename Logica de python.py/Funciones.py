# A qui definere todas las funciones.
import csv

# Paso 1: Abrir el csv.
def abrir_csv():
    with open('people_list.csv', mode='r', encoding='utf-8', newline='') as archivos_csv:
        datoscsv = csv.DictReader(archivos_csv)
        return(list(datoscsv))
    
def leer_csv():
    datos = abrir_csv()

    for linea in datos:
        print(linea)


#   Paso 2: Crear persona en el csv:
def crear_persona_csv():
    datos = abrir_csv()

    nueva_persona = {'DNI':input("Ingrese un dni: "),
                     'Nombre':input("Ingrese un nombre: "),
                     'Edad':input("Ingrese una edad: ")
                     }    
    datos.append(nueva_persona)

    with open('people_list.csv', mode='w', encoding='utf-8', newline='') as archivos_csv:
        datos_escribir = csv.DictWriter(archivos_csv,fieldnames=['DNI','Nombre','Edad'])
        datos_escribir.writeheader()
        datos_escribir.writerows(datos)
        print("Pesona preada correctamente. ")

# paso 3: actualizar persona en el csv.
def actualizar_persona_csv():
    datos = abrir_csv()
    dni = input("Ingres el DNI de la persona a actualizar: ")
    persona_encontrada = False

    for persona in datos:
        if persona['DNI'] == dni:
            persona['Nombre'] = input("Ingrese el nuevo Nombre: ")
            persona['Edad'] = input("Ingrese la nueva Edad: ")
            persona_encontrada = True

    if persona_encontrada:
        with open('people_list.csv', mode='w', encoding='utf-8', newline='') as archivos_csv:
            datos_escribir = csv.DictWriter(archivos_csv, fieldnames=['DNI', 'Nombre', 'Edad'])
            datos_escribir.writeheader()
            datos_escribir.writerows(datos)
            print("persona actualizada correctamente.")
    if not persona_encontrada:
        print("Persona con DNI {} no encontrada.".format(dni))

# Paso 4: Eliminar una persona en el csv.
def eliminar_persona_csv():
    datos = abrir_csv()
    dni = input("Ingrese el dni de la persona a eliminar: ")
    datos_filtrados = [persona for persona in datos if persona['DNI'] != dni]

    if len(datos) == len(datos_filtrados):
        print("Persona con DNI {} no encontrada".format(dni))
    else:
        with open('people_list.csv', mode='w', encoding='utf-8', newline='') as archivos_csv:
            datos_escribir = csv.DictWriter(archivos_csv, fieldnames=['DNI', 'Nombre', 'Edad'])
            datos_escribir.writeheader()
            datos_escribir.writerows(datos_filtrados)
            print("Persona eliminada correctamente.")

# Paso 5: Buscar persona en el csv.
def buscar_persona_csv():
    datos = abrir_csv()
    dni = input("Ingrese el DNI de la persona que desea encontrar: ")
    persona_encontrada = False

    for persona in datos:
        if persona ['DNI'] == dni:
            print(f"Persona encontrada: {persona}")
            persona_encontrada = True
            break

    if not persona_encontrada:
        print(f"Persona con DNI {dni} NO ENCONTRADA.")



def preguntas_frecuentes():
    print()






# USOS de las definiciones.

# leer_csv()
# crear_persona_csv()
# actualizar_persona_csv()
# eliminar_persona_csv()
# buscar_persona_csv()
