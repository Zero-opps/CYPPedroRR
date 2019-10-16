EDAD= int(input("\nIngresa los años del paciente: "))
TIPO= int(input("Tipo de enfermedad: "))
DIAS= int(input("Dias en el hospital: "))
COSTOT=0.0
if EDAD >= 14 and EDAD <= 22:
    if TIPO==1:
        COSTOT= DIAS*25*1.10
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==2:
        COSTOT= DIAS*16*1.10
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==3:
        COSTOT= DIAS*20*1.10
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==4:
        COSTOT= DIAS*32*1.10
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
else:
    if TIPO==1:
        COSTOT= DIAS*25
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==2:
        COSTOT= DIAS*16
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==3:
        COSTOT= DIAS*20
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
    if TIPO==4:
        COSTOT= DIAS*32
        print(f"\nEL paciente con enfermedad tipo {TIPO}, edad {EDAD}, {DIAS} dias en el hopital, debe pagar: ${COSTOT} .")
print("\nFinaliza cálculo de los gastos del hospital ")
