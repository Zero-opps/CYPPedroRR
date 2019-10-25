NUM= int(input("\nIntroduce el numero de interación en la secuencia de FIBONACCI: "))

PR= 0
SEG= 1

for i in range (3,NUM+1,1):
    SIG= PR+SEG
    PR=SEG
    SEG= SIG
    i+= 1

print(f"\nEl término número {NUM} de de la secuencia es: {SIG} .")

print("-\nFinaliza el programa .")
