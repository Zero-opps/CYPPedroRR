import math #se importa la biblioteca

Alfa = float(int(input("\nIngresa un angulo alfa: ")))
Radian = math.radians(Alfa) # función-tranforma-grados-->radianes

sen = math.sin(Radian)
cos = math.cos(Radian)


print(f"\nFunciones trigonométricas del ángulo: {Alfa}° :")
print(f"\n    sen de {Alfa} es: {sen} ")
print(f"    cos de {Alfa} es: {cos} ")
tan= sen/cos
print(f"    tan de {Alfa} es: {tan} ")

print("\nFinaliza el programa .")
