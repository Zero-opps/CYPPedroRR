NUM=int(input("\nNuméro de elementos de la lista <= 500 : "))
print("\n°")
VEC=[]


if NUM>=1 and NUM<=500:

    for i in range (NUM):
        VEC.append(int(input(" Ingresa un numero: "))) 
    VEC.sort () # se ordenan los numeros ascendentemente para que el "último while" pueda descartar los valores repetidos.
    print(f"\nLista ascendente de numeros: {VEC} .")
    print("\nLista de numeros sin repeticiones:")
    
    i=0   # cadena "VEC", " i=0 ", por ser el primer valor de la lista"
    while i<=NUM-1:  # " NUM-1 " ya que " VEC=lista de elementos ", " 1er elemento 1 = posición 0 "
        print(VEC[i])
        REPET=VEC[i]
        while i<=NUM-1 and REPET==VEC[i]: # while encargado de mantener la sumatoria en "i" y descartando los valores repetidos 
            i+=1

else:
    print("\n El numero de elementos de la lista es inorrecto .")

print("\n Fin del programa .")
