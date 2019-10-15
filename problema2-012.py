CAT=int(input("Ingresa tu categoria de trabajador (1-4): "))
SUE=int(input("Ingresa tu sueldo: "))
EXT=int(input("Horas extras trabajadas: "))
total=0
if CAT==1:
    total=SUE+(EXT*30)
    print(f"Tu pago es de: ${total} .")
elif CAT==2:
    total=SUE+(EXT*38)
    print(f"Tu pago es de: ${total} .")
elif CAT==3:
    total=SUE+(EXT*50)
    print(f"Tu pago es de: ${total} .")
elif CAT==4:
    total=SUE+(EXT*70)
    print(f"Tu pago es de: ${total} .")
else:
    print("Su pago permanece igual: {SUE} .")
print("Finalizan el ajuste al sueldo .")
