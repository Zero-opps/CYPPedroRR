#Index
nombre = "Clank Jack"
print (f"\n{nombre}")
print (nombre [0])
print (nombre [7])
print (nombre [-1])
print (nombre [-4])

#Slicing
print (nombre [1:4:2])
#Valores por defecto del slicing, [6: :1] "tamaño-cadena" ; [ : : :] "0":"9":"1" 
print (nombre [6: :1])
print (nombre [ : : ])
print (nombre [ :5: ])
print (nombre [0:5:2])
#Slicing negativo       
print (nombre [-1:-5:-1])
print (nombre [ : :-1])
print (nombre [-6:-11:-1])
print (nombre [-6: :-1])


#Hacer los ejercicios indicados con la siguiente frase

frase = "Solo existen 10 tipos de personas, las que saben binario y las que no"

#Hacer un slicing para imprimir la palabra: existen
#Otro para imprimir la palbra: personas en orden inverso = sanosrep
#Hacer un slingin que imprima toda la cadena en orden inverso

print (frase [5:12:1])
print (frase [-37:-45:-1])
print (frase [ : :-1])

