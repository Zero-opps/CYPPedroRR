print("\nElija un número de la elección del voto, deacuerdo al candidato: ")

CAN1= 0.0
CAN2= 0.0
CAN3= 0.0
CAN4= 0.0

VOTOS=0

VOTO=int(input("1=Candidato 1° , 2=Candidato 2°, 3=Candidato 3°, 4=Candidato 4°: "))

while VOTO != 0:
    if VOTO==1:
        CAN1+=1
    if VOTO==2:
        CAN2+=1
    if VOTO==3:
        CAN3+=1
    if VOTO==4:
        CAN4+=1
    VOTOS+=1
    VOTO= int(input("Voto (ingresa '0', si no hay más votos : "))

TOTAL= CAN1+CAN2+CAN3+CAN4

print(f"\nVotos para el candidato 1°: {CAN1} , porcentaje de votos: {CAN1/TOTAL*100.00} ")
print(f"Votos para el candidato 2°: {CAN2} , porcentaje de votos: {CAN2/TOTAL*100.00} ")
print(f"Votos para el candidato 3°: {CAN3} , porcentaje de votos: {CAN3/TOTAL*100.00} ")
print(f"Votos para el candidato 4°: {CAN4} , porcentaje de votos: {CAN4/TOTAL*100.00} ")

print("-\nFinaliza el programa .")

