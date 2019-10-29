llamada= True

NumI= 0
costoI= 0

NumN= 0
costoN= 0

NumL= 0
costoL= 0


CL= 0
CUENTA= 0

while (llamada==True):
    Zona= str(input("\nIngresa la 'inicial, deacuerdo al tipo de llamada ('I'-internaciona 'N'-nacional 'L'-local) : "))
    Min= int(input("Minutos de llamada: "))
    
    if Zona == 'I':
        if Min > 3:
            costo = 7.59+(Min-3)*(3.03)
        else:
            costo = 7.59
        NumI+=1
        costoI+=costo
    if Zona == 'L':
        CL+=1
        if CL > 50:
            costo = 0.60
        else:
            costo = 0
        NumL+=1
        costoL+=costo
    if Zona == 'N':
        if Min > 3:
            costo = 1.20+((Min-3)*(0.48))
        else:
            costo = 0.48
        NumN+=1
        costoN+=costo
    CUENTA += costo

    llamada = bool(int(input("\nIngresa '1' para calcular otra llamada, '0' para finalizar : ")))

print("\nSe realizaron: ")
print(f"\n {NumI} llamadas internacionales, con un costo total de: ${costoI} .")
print(f" {NumN} llamadas nacionales, con un costo total de: ${costoN} .")
print(f" {NumL} llamadas locales, con un costo total de: ${costoL} .")
print(f"\nEl precio total por las llamadas es de: ${CUENTA} .")
print("-\nFinaliza el programa .")
