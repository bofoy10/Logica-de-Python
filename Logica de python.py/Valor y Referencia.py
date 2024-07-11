print("""
    +================+
    |      Valor     |
    |        y       |
    |   Referencia   |
    +================+ 
          """)






# tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30 
print(my_int_a)
print(my_int_b)

# tipos de dato por referencia "heredan posicion de memoria, a y b son independientes de si mismo"

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# funciones con datos por valor 

my_int = 10

def my_numerito(my_int: int):
    my_int = 20
    print(my_int)

my_numerito(my_int)
print(my_int)

# funcion con datos de referencia

my_list = [10, 20]

def my_list_fun(my_list :list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_fun(my_list_c)
print(my_list_c)



# Ejemplo por valor


def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# por referencia

def value(value_a: int, value_b: int) -> tuple:
     temp = value_a
     value_a = value_b
     value_b = temp
     return value_a, value_b


my_int_d = [10, 20]
my_int_e = [30, 40]
my_int_f, my_int_g = value(my_int_d, my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")
