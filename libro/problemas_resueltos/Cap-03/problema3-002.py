NUM= 2.0
TOTAL= 0.0
BAND= 'W'
while (NUM<=1800):
    TOTAL+=NUM
    print(NUM)
    if BAND=='W':
        BAND='Y'
        NUM+=3
    else:
        BAND='W'
        NUM+=2
print("\nLa suma de los números de la serie anterio es: ",TOTAL)
print("\nFinaliza el programa")
