CAT=int(input("\nIngresa tu categoria de trabajador (1-4): "))
SUE=int(input("Ingresa tu sueldo: "))
EXT=int(input("Horas extras trabajadas: "))
total=0
if CAT==1:
      if EXT<=30:
            total=SUE+(EXT*30)
            print(f"\nTu pago es de: ${total} .")
      else:
            total=SUE+(30*30)
            print(f"\nTu pago es de: ${total} .")
elif CAT==2:
      if EXT<=30:
            total=SUE+(EXT*38)
            print(f"\nTu pago es de: ${total} .")
      else:
            total=SUE+(30*38)
            print(f"\nTu pago es de ${total} .")
elif CAT==3:
      if EXT<=30:
            total=SUE+(EXT*50)
            print(f"\nTu pago es de: ${total} .")
      else:
            total=SUE+(30*50)
            print(f"\nTu pago es de ${total} .")
elif CAT==4:
      if EXT<=30:
            total=SUE+(EXT*70)
            print(f"\nTu pago es de: ${total} .")
      else:
            total=SUE+(30*70)
            print(f"\nTu pago es de ${total} .")
else:
      print("\nSu pago permanece igual: {SUE} .")
print("-\nFinalizan el ajuste al sueldo .")
