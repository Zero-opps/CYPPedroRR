#Listas

lluvias_norte=[80,60,120,100,70,150,100,47,95,70,100,130]
print("\n")

for indice in range(0,12,1):
    print(f" mes { indice+1 } en regiòn norte= { lluvias_norte [indice] } ")

print(f"\n {lluvias_norte[4]} ")
print(lluvias_norte[::-1])
print(lluvias_norte[:11:-1])

sueldos= []

suma= 0

for i in range (7):
    sueldos.append(int(input("Sueldos: ")))

print(sueldos)

for indice in range(7):
    suma+=sueldos[indice]

promedio= suma/7
print(f"El promedio de los sueldos es: {promedio}")
cont=0

for indice in range(7):
    if sueldos[indice] > promedio:
        cont+=1
        print(f"Arriba: { sueldos[indice] }")
    
