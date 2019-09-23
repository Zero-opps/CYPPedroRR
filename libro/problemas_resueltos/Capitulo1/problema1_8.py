print("Ingresa las coordenadas de un punto A, en un plano 'x' 'y' .")
X1= float(input("Coordenada x1: "))
Y1= float(input("Coordenada y1: "))
print("A hora las coordenas de un punto B : ")
X2= float(input("x2: ")) 
Y2= float(input("y2: "))
DIS= (((X2-X1)**2)+((Y2-Y1)**2))**.5
print(f"La distancia etre los puntos: A {X1,Y1}  y  B {X2,Y2}, es:  {DIS} .")

