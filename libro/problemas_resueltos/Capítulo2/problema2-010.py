a= int(input("Ingresa un nùmero: "))
b= int(input("Ingresa un nùmero: "))
c= int(input("Ingresa un nùmero: "))
if a>b:
    if a>c:
        print(f"A es el mayor con valor {a} .")
    elif a==c:
        print(f"A y C son iguales, y los mayores con valor{c} {a} .")
    else:
        print(f"{c} es el mayor")
elif a==b:
    if a>c:
        print(f"A y B son los mayores con valor {a} .")
    elif a==c:
        print(f"A,B,C son iguales con valor {a} .")
    else:
        print(f"C es el mayor, con valor {c} .")
elif b>c:
    print(f"B es el mayor con valor {b}")
elif b==c:
    print(f" B y C son los mayores con valor {c} .")
else:
    print(f"C es el mayor con valor {c} .")
print("Termina el programa .")
