print("""
    +================+
    |    FUNCIONES   |
    |    DEFINIDAS   |
    |     POR El     |
    |     USUARIO    |
    +================+ 
          """)

# Simple

def greet():
    print("Hola, python!")

greet()

# Con Retorno 

def debuelve_saludo():
    return "Hola, python!"

greet = (debuelve_saludo())

# Con un Argumento

def arg_greet(nombre):
    print(f"Hola, {nombre}!")

arg_greet("Jean")

# Con argumentos

def arg_greet(greet, nombre):
    print(f"Hola, {greet},{nombre}!")

arg_greet("Hola", "Jean")
arg_greet(nombre="jean", greet="hola")

# Con Argumento Predeterminado

def Pdefecto_arg_greet(nombre= "Python"):
    print(f"Hola, {nombre}!")

Pdefecto_arg_greet("Jean")

# Con Argumentos y Retorno

def retorno_args_greet(greet, nombre):
   return f"{greet}, {nombre}!"

print(retorno_args_greet("Hola", "Jean"))

# Con Retorno de Varios Valores

def multiple_return_greet():
    return "Hola", "Python"

greet, nombre = multiple_return_greet()
print(greet)
print(nombre)

# Con un numero variable de argumentos

def variable_arg_greet(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

variable_arg_greet("Python", "Jean", "bofoy", 18)

# Con numero variable de argumentos con palabras clave

def variable_key_arg_greet(**nombres):
    for key, value in nombres.items():
        print(f"{value}! ({key})")

variable_key_arg_greet(
    lenguaje="Python",
    nombre="Jean",
    alias="bofoy",
    edad=18
)


print("""
    +================+
    |     FUNCION    |
    |    DENTRO DE   |
    |     FUNCION    |
    |                |
    +================+ 
          """)

def outer_funcion():
    def inner_funcion():
        print("Funcion interna: Hola, Python!")
    inner_funcion()

outer_funcion()



print("""
    +================+
    |     FUNCION    |
    |       DEL      |
    |    LENGUAJE()  |
    +================+ 
          """)


print(len("hola papito"))
print(type("hola papito"))
print(type(18))
print("Hola papito".upper())


print("""
    +================+
    |     FUNCION    |
    |      LOCAL     |
    |        Y       |
    |      GLOBAL    |
    +================+ 
          """)

variable_global = "Python"


print(variable_global)

def hola_Python():
    variable_local = "Hola"
    print(f"{variable_local}, {variable_global}!")

print(variable_global)
# print(variable_local) no se puede usar fuera de una funcion

hola_Python()


print("""
    +================+
    |      TAREA     |
    +================+ 
          """)

def print_numeros(multiplo3, multiplo5)-> int:
    count = 0 
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(multiplo3 + multiplo5)
        elif numero % 3 == 0:
            print(multiplo3)
        elif numero % 5 == 0:
            print(multiplo5)
        else:
            print(numero)
            count +=1
    return count 
    
print(print_numeros("multiplo 3", "multiplo 5"))
