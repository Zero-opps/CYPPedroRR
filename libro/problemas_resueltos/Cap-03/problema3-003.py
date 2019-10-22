N=int(input("Ingresa un número entero: "))
A=1.0
SUM=0.0
BAND= 'T'
while (A<=N):
    if BAND=='T':
        SUM+=(1/A)
        BAND='Y'
    else:
        SUM-=(1/A)
        BAND='T'
    A+=1
print(SUM)
