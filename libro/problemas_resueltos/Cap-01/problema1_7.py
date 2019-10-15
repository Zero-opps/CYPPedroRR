print("Ingresa tres lados de un triángulo .")
a= float(input('El lado "a" mide : '))
b= float(input('Lado "b" : '))
c= float(input('Lado "c" : '))
S= (a+b+c)/2
A= (S*(S-a)*(S-b)*(S-c))**(1/2)
print(f"El semiperímetro de este triángulo es: {S} cm y su área es igual a: {A} cm\u00b3 .")
