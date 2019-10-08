CATE= int(input("Ingresa tu categoria (1-4): "))
SUE= int(input("Ingresa tu sueldo: "))
NSUE= 0
if CATE==1:
    NSUE= SUE * 1.15
elif CATE==2:
    NSUE= SUE * 1.10
elif CATE==3:
    NSUE= SUE * 1.08
elif CATE==4:
    NSUE= SUE * 1.07
else:
    print("Ingresa una clase valida")
print(f"La categoria del trabajador es {CATE} y su nuevo sueldo es ${NSUE} .")

