# print tiene cuatro formas de us
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format ()
4.- Es con una variante de format ()
"""
# con comas
# concatenar agregando un espacio y haciendo casting tipo
edad = 10
nombre = "Juan"
estatura= 1.67

print(edad, estatura, nombre)

#con signo + hace lo mismo pero no realiza el casting automàtico
#no agrega espacios

print(str(edad) + str(estatura) + nombre)

# funcion format()

print("Nombre: {1} Edad: {0}".format(nombre, edad, estatura))

# 4.- Es con una variante de format () simplificada

print(f"Nombre: \"{nombre}\" \nEdad:\t{edad}")

# Print caracter de escape diagonal invertida, si se ejecuta significa salto de linea, diagonal t
# \" caracter de escape se usa para ingresar texto que no pertence al còdigo
# \n \.
# print y el argumento end
print("Solo hay 10 tipos de personas las que saben binario y las que no",end="---")
print("otra linea")

for x in range(0,n,1)
    print(f"+", end=")
