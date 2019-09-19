NOM=str(input("Dame el nombre del dinosaurio: "))
PES=int(input("Dame su peso en kg"))
LON=int(input("Dame su altura en metros"))
T=1000
P=0.3047
PESKIL= PES*T
LONMET= LON*P
print(f"El nombre del dinoaurio es {NOM}, su peso es {PESKIL}kg y su altura {LON}pies.")
