print("\nIngresa los valores para la ecuación de la forma: ax\u00b2 + bx + c = 0 .") 

a = float(input("\nIngresa 'a': "))
b = float(input("Ingresa 'b': "))
c = float(input("Ingresa 'c': "))

print(f"\nDe la ecuación: {a}x\u00b2 + {b}x + {c} = 0 , se obtiene que: ")

radicando = (b**2)-(4*a*c)


if radicando > 0:
    X1 = (-b+(radicando)**.5)/(2*a)
    X2 = (-b-(radicando)**.5)/(2*a)
    print(f"\nLas raíces reales son {X1} , {X2} .")

else:
    print("\nLas raíces no son reales, el radicando queda negativo en la formula general .")

print("\nEl análisis finalizó")
