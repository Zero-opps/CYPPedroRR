nombre = "Clank Jack"
frase = "Solo existen 10 tipos de personas las que saben binario y las que no"
user = "project omicron letter"

# print (dir (nombre) ) -----> muestra-funciones

# find
print ("\nFunciones de string (str) ")
print (nombre.upper ())
print (f"\nLa palabra: 'existen' de la frase, está en la pos. {frase.find ('existen')}")
print (f"\nLa palabra: 'saben' de la frase, está en la pos. {frase.find ('saben')}")
# replace
print(f"\nLa frase modificada es: {frase.replace ('binario', 'octal')}.")
print(frase)
# capitalize
print(f"\n Welcom: {user.capitalize()}")
# title
print(f"\n Welcom: {user.title()}")
# upper
print(f"\nFrase: {frase.upper()}")
# lower
print(f"Frase: {frase.lower()}")
# count
print(f"\n¿Cuántas letras 'o' tiene en total la frase anterior? {frase.count('o')}")
# center
print(nombre.center(100,'*'))
