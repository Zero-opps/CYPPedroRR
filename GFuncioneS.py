def sumar(x,y):
    z=x+y
    return z

def restar (x,y):
    return x-y
def mi_print (texto):
    print(f"Este es mi print ; {texto} ")
def multiplica(valor,veces):
    if veces==None:
        print("Debes enviar el segundo argumento de la función")
    else:
        print(valor*veces)

def comanda(mesa,comensal,entrada,medio,fuerte,postre="Gelatina de limòn"): # argumentos(-variables-valores demtro de la función)
    
    print(f"Mesa: {mesa} comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte} ")
    print(f"\t Postre: {postre}")

def comanda2(**comida):
    llaves=comida.keys()
    for elem in llaves:
        print("->",comida(elem)) #Sustituir por corchetes
    print(comida)

def imprime_argumentos(*argumentos):
    print('----->',argumentos,'<-----')
    for ele in argumentos:
        print(ele)
    for index in range (len(argumentos)):
    print(argumentos(index)#sustituir parentisis por corchetes 

a=10
b=5
c=sumar(a,b,)


print(f"La suma de {a} y {b} es {c}")
c=restar(a,b)

print(f"\n La resta de {a} y {b} es {c}")


#(Parámetros-función llamada)

mi_print ("Hola!!!")

multiplica(1,3)
multiplica(10,None) # Valor None la función hace el print después del if
multiplica('Hola',3)

comanda(2,1,"Ensalada","Sopa de rana","Filete de oso","Flan")
comanda("Ensalada","Sopa de rana","Filete de oso","Flan",2,1)
comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de oso",postre="Flan",mesa=2,comensal=1)
comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de oso",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'Juan'})
imprime_argumentos()
comanda2(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de oso",mesa=2,comensal=1)

