print("""
    +================+
    |                |
    |   OPERADORES   |
    |                |
    +================+ 
          """)

# Operadores Aritmeticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"divición: 10 / 3 = {10 / 3}")
print(f"potencia: 10 ** 3 = {10 ** 3 }")
print(f"porcentaje: 10 % 3 = {10 % 3}")
print(f"divicion entera: 10 // 3 = {10 //3}")

# Operadores de Comparación

print(f"Igualdad: 10 == 3 es = {10 == 3}")
print(f"Desigualdad: 10 != 3 = {10 != 3}")
print(f"Mayor que 10: > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 {10 <= 3}")

# Operadores Logicos

print(f"AND : 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") 
print(f"NOT: 10 + 3 == 14 es {not 10 + 3 ==14}")

# Operadores de Asignacion

my_numero = 11 # Asignacion
print(my_numero)
my_numero += 1 # Suma y Asignacion 
print(my_numero)
my_numero -= 1 # Resta y Asignacion
print(my_numero)
my_numero *= 1 # Multiplicacion y Asignacion
print(my_numero)
my_numero /= 1 # Divicion y Asignacion
print(my_numero)
my_numero %= 1 # Porcentaje y Asignacion
print(my_numero)
my_numero **= 1 # Potencia y Asignacion
print(my_numero)

# Operadores de Identidad
#  
my_nuevo_numero = my_numero
print(f"my_numero is my_nuevo_numero es {my_numero is my_nuevo_numero}")
print(f"my_numero is my_nuevo_numero es {my_numero is not my_nuevo_numero}")

# Operadores de Pertenencia

print(f"'u' in 'moure' = {'u' in 'moure'}")
print(f"'b' in 'moure' = {'b' not in 'moure'}")

# Operadores de Bit

a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3} ")  # 0010
print(f"OR: 10 | 3 = {10 | 3} ")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3} ")  # 1001 
print(f"NOT: ~10 = {~10} ")
print(f"Desplasamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplasamiento a la derecha: 10 << 2 = {10 << 2}") # 0010

print("""
    +================+
    |   ESTRUCTURA   |
    |       DE       |
    |    CONTROL     |
    +================+ 
          """)

# Condicionales

my_strinmg ="braise" 
if my_strinmg == "MoureDev":
    print("my_strinmg es 'MoureDev")
elif my_strinmg == "braise":
    print("my_stinmg es braise")
else:
    print("my_strinmg no es 'MaureDev ni 'braise")

# Interactivas

for i in range(11):
    print(i)
i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de Excepciones

try:
    print(10/3)
except:
    print("Se a prosucido un error")
finally:
    print("Ha finalizado el manejo de exepciones")

print("""
    +================+
    |                |
    |      TAREA     |
    |                |
    +================+ 
          """)

for numero in range(10,56):
    if numero % 2 == 0 and numero != 16 and numero %3 != 0:
        print(numero)