# Ejercicio, Muestra ejemplos de creacion de todas las estructuras soportadas por defecto en tu lenguaje.
# Utiliza operaciones de incercion, borrado, actualizacion, ordenacion. 
print("""
    +================+
    |                |
    |   ESTRUCTURAS  |
    |                |
    +================+ 
          """)


# Lista.
my_lista = ["Empoleon", "Suamper", "Mamoswain", "Geratina"]
print(my_lista)
my_lista.append("Charizart") #Insercion: Añade el nombre al final.
print(my_lista)
my_lista.remove("Empoleon") # Eliminacion
print(my_lista)
print(my_lista[1])
my_lista[1] = "Gyarados" # Actualizacion
print(my_lista) 
my_lista.sort() # Orientacion: orden alfabetico o en caso de numeros de forma acendente.
print(my_lista)
print(type(my_lista))

# Tuplas, son inmutables
my_tupla = ("Jean", "Valenzuela", "@bofoy", "18")
sorted(my_tupla)
my_tupla = tuple(sorted(my_tupla)) # Orientacion, trasforma la tupla en lista y luego la vuelve a convertir en tupla
print(my_tupla)
print(type(my_tupla))

# Sets, estructura desordenada
my_set = {"Jean", "Valenzuela", "@bofoy", "18"}
print(my_set)
my_set.add("bofoy@gmail.com")  #Insercion : los sets evitan la repeticion de datos
my_set.add("bofoy@gmail.com")
my_set.remove("Jean") # Eliminar
print(my_set)
my_set = set(sorted(my_set)) # No se puede Ordenar
print(my_set)
print(type(my_set))

# Dicionario
my_dict: dict = {
    "name":"Jean",
    "apellido":"Valenzuela",
    "alias":"@bofoy", 
    "edad":"18"

}
my_dict["email"] = "bofoy@gamil.com" # Incercion
print(my_dict)
del my_dict["apellido"] # Eliminacion
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["edad"] = "19" # Actualizacion
my_dict = dict(sorted(my_dict.items())) # Ordenacion= sorted: transforma en lista, .items: toma todo de la lista y separa, dict: vuelve todo un diccionario
print(my_dict)
print(type(my_dict))


# Ejercicio 

def my_Telefono():

    agenda = {}

    def insert_contact():
            phone = input("Introduce el Telefono del contacto: ")
            if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
            else:
                print(
                    "Deves introducir un numero de telefono con maximo 11 digitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Incertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nselecciona una opcion: ")

        match opcion:
            case "1":
                name = input("Introduce el nombre a buscar: ")
                if name in agenda:
                    print(
                        f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Intruduce el Nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
                name = input("Introduce el nombre a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print("El contacto no existe")
            case "5":
                print("Saliendo de la ajenda")
                break
            case _:
                print("Opcion no valida, elije una opcion del 1-5.")


my_Telefono()