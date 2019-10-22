
ARNO=0
ARCE=0
ARSU=0
MERSU=50000
MES=0
MES=0

for i in range (1,13,1):
    print(f"Mes {i}:")
    RNO=int(input('Promedio de lluvias en la zona Norte: '))
    RCE=int(input('Promedio de lluvias en la zona Cenro: '))
    RSU=int(input('Promedio de lluvias en la zona Sur: '))

    ARNO += RNO 
    ARCE += RCE
    ARSU += RSU

    if RSU<MERSU:
        MERSU =RSU
        MES = i

PRORCE = ARCE/12
print(f"Promedio region centro:{PROCE} ")
print(f"Mes con menor lluvia  reg. Sur: {MES}")
print(f"Registro con menor lluvia del mes: {MERSU}")

if ARNO>ARSU:
    if ARNO>ARSU:
        print("La regiòn con mayor lluvia es la regiòn Norte . ")
    else:
        print("La regiòn con mayor lluvia es la regiòn Sur .")
elif ARCE>ARSU:
    print("La regiòn con mayores lluvias es la regiòn Centro.")
else:
    print("La regiòn con mayores lluvias es la regiòn Sur .")

print("Fin del programa !!!")
