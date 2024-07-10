print("""
    +================+
    |                |
    |   Operaciones  |
    |                |
    +================+ 
          """)

s1 = "hola"
s2 = "python"

# Concatenacion
print(s1 + "," + s2 + ".")

# Repeticion
print(s1 *3)

# Indecsacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Porcion
print(s2[2:6])
print(s2[2:])
print(s2[:2])

# Busqueda
print("ho" in s1)
print("i" in s1)

# Remplazar 
print(s1.replace("o", "a"))

# Divicion
print(s2.split("t"))

# Mayusculas y minusculas
print(s1.upper())
print(s2.lower())
print("jean pierre".title())
print("jean pierre".capitalize())

s3 = "Jean pierre @bodoy"

# Eliminacion de espacion al principio y al final
print(" jean pierre ".strip() + " @bofoy ")

# Busqueda al principio y al final
print(s1.startswith("ho"))
print(s1.startswith("py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

# Busqueda de posiscion
print(s3.find("Jean"))
print(s3.find("Jean"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Busqueda de ocurrencia
print(s3.lower().find("m"))

# Formateo 
print("salido:{} , lenguaje: {}!".format(s1,s2))

# Interpolacion 
print(f"salido:{s1} , lenguaje: {s2}!")

# Transformacion en lista de caracteres
print(list(s3))

# Transformar lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "12345"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

# Ejemplo

def check(word1: str, word2: str):

    # Palindromo
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")
    
    # Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    
check("radar, python")
check("amor", "roma")