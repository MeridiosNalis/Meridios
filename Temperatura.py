while True:
  try:
    temperatura = int(input("Ingresa un Temperatura: "))
    break
  except ValueError:
    print("Error: Ingresa un número valido.")

if 25 <= temperatura <=45:
  print(f'Cuidado con quemarse papi')
elif 15 <= temperatura < 25:
  print(f'Preparese papi, el frío viene')
elif 0 <= temperatura < 15:
    print(f'Hace frío')
elif temperatura < 0:
    print("AAAAAAA, me congelo")
else:
    print("☠")
