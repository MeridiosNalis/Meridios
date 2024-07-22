'''
def validar_positivo(num, num_2):
    if all(x >= 0 for x in (num, num_2)):
        return f'Los valores {num} y {num_2} son positivos'
    else:
        return f'Los valores {num} y {num_2} son negativos'

num = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese un segundo número: "))

print(validar_positivo(num, num_2))
'''

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 130:
            print("ERROR con el valor indicado")
        else:
            break
    except:
        print("Formato o valor inválido ")
        
while True:
    try:
        credencial = input('¿Posee documento de identidad vigente? ["si"]["no"]: ')
        if credencial == "si" or credencial == "no":
            break
        else:
            print("Elección inválida")
    except ValueError:
        print("Formato o valor inválido")

if edad >= 18 and credencial == "si":
    print("Estás apto para votar mi rey")
else:
    print("NO ESTÁS APTO, PA LA CASA")