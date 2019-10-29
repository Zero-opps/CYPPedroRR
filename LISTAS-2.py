#Arreglos
#Lectura
#Escritura/Asignaciòn
#Actualizaciòn: inserciòn, eliminaciòn, modificaciòn
#Ordenamiento
#busqueda

#escritura
frutas=["Zapote","Manzna", "Pera", "Aguacate", "Durazno", "Uva", "Sandia"]

#lectura
print(frutas[2])

#lectura con for

#for opcciòn 1
for indice in range (0,7,1):
    print(frutas[indice])

print("-------")

#for opcciòn 2 -- por un iterador for each (variable tipo interno)
for fr in frutas:
    print(fr)

#Asignaciòn--Cambia el elemento por otro (Pera-Melòn)
frutas[2]="Melòn"
print(frutas)

#Inserciòn al fina -Append
frutas.append("Naranja")
print(frutas)
print(len(frutas))

##dir(list)- muestra las funciones
## help(list.insert) ----> help(list."función a obtener su uso")

frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))

frutas.insert(0,"Mamey")
print(frutas)

#eliminación con pop, saca el elemento entre() lo imprime, e imprime la nueva lista
print(frutas.pop())
print(frutas)

print(frutas.pop(1))
print(frutas)


frutas.append("Limón")
print(frutas)
frutas.remove("Limón")
print(frutas)

# Ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# busquedad
print(f"La uva está en la pos. {frutas.index('Uva') } ")
print(f"El limón esta { frutas.count('Limón') } veces en la lista")

#Concatenar
print(frutas)
otras_frutas = ["Rambutan","Nispero","Linche","Pitahaya"]
frutas.append(otras_frutas)
print(frutas)

frutas.extend(otras_frutas)
print(frutas)

# Copiar

copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia= frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
