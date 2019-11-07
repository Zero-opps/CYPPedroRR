def sumar(x,y):
    z=x+y
    return z

def restar (x,y):
    return x-y

def main ():
    a=10
    b=5
    c=sumar(a,b,)
    print(f"La suma de {a} y {b} es {c}")
    c=restar(a,b)
    print(f"La restar de {a} y {b} es {c}")

#
    
if __name__=='__main__':#¿Se mandò a ejecutar (interpretar) este archivo?
    main()

