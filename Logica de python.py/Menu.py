# Paso 1: Importar los archivos nesesarios.
import csv
import Funciones

# Paso 2: Crear el menu.
def mostrar_menu():

    print("""\n
            +===============+
            |   VIENBENIDO  |
            |   A LA BASE   |
            |       DE      |
            |     DATOS     |
            +===============+
          """)
    print("[1.]📄 Leer csv.")
    print("[2.]🔍 Buscar persona.")
    print("[3.]➕ Crear persona.")
    print("[4.]🔄️ Actualizar persona.")
    print("[5.]🗑️  Eliminar persona.")
    print("[6.]❓ Preguntas frecuentes.]")
    print("[7.]🚪 Salir.")

# paso 3: Definir las opciones del menu.
def ejecutar_opcion(opcion):
    if opcion == '1':
        print("\n📄 Leyendo csv...")
        Funciones.leer_csv()

    elif opcion == '2':
        print("\n🔍 Buscando persona...")
        Funciones.buscar_persona_csv()

    elif opcion == '3':
        print("\n ➕ Crear persona...")
        Funciones.crear_persona_csv()

    elif opcion == '4':
        print("\n🔄️ Actualizar persona...")
        Funciones.actualizar_persona_csv()

    elif opcion == '5':
        print("\n🗑️  Eliminando persona...")
        Funciones.eliminar_persona_csv()

    elif opcion == '6':
        print("Respondiendo las preguntas frecuentes...")
        Funciones.preguntas_frecuentes()

    elif opcion == '7':
        print("\n🚪 Saliendo...")
        return False
    else:
        print("\n⚠️ Opcion Incorrecta, POR FAVOR elija una de las seis opciones.")
    return True

# Paso 4: definir el punto de entrada usando def main(): para organizar el código y hacer que sea más claro y mantenible.  
# Explicacion de Main.  
def main(): # Organiza el codigo.
    continuar = True

    while continuar: # Main() contiene un bucle while que permite que el menú se muestre repetidamente hasta que el usuario decida salir.
        mostrar_menu()
        opcion = input("Elija una de las seis opciones: ")
        continuar = ejecutar_opcion(opcion)

if __name__ == "__main__": # Al utilizar if __name__ == "__main__":, Python puede determinar si el script se está ejecutando directamente 
    main()                 # o si se está importando como módulo.
                           # Si se está ejecutando directamente, se llama a main(). Si se importa, main() no se ejecutará automáticamente.