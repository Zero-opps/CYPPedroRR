NUM_1 = int(input("Dame un nùmero: "))
NUM_2 = int(input("Dame un nùmero: "))
NUM_3 = int(input("Dame un nùmero: "))

if NUM_1 > NUM_2 and NUM_1 > NUM_3:
    print(f"{NUM_1} es el nùmero mayor: ")

if NUM_2 > NUM_1 and NUM_2 > NUM_3:
    print(f"{NUM_2} es el nùmero mayor: ")
    
if NUM_3 > NUM_1 and NUM_3 > NUM_1:
    print(f"{NUM_3} es el nùmero mayor: ")
    
print("Fin del programa")
