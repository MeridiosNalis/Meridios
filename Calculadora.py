num = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

def  calculadora(num, num2):
    return (f'La suma ({num} + {num2}) es: {num + num2}\n'
    f'La resta ({num} - {num2}) es: {num - num2}\n'
    f'La multiplicación ({num} * {num2}) es: {num * num2}\n'
    f'La división ({num} / {num2}) es: {num / num2}\n'
    f'La división entera ({num} // {num2}) es: {num // num2}\n'
    f'La división con módulo ({num} % {num2}) es: {num % num2}\n'
    f'El valor exponencial ({num} ** {num2}) es: {num ** num2}')

print(calculadora(num, num2))