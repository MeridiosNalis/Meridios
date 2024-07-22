lista = ["Beat It - Michael Jackson", "Know You Better - Black Pumas", "Leave The Door Open - Bruno Mars, Anderson.Paak, Silk Sonic",
"I'll Be There For You - Bon Jovi", "I'm Still Standing - Elton John"]
for x in range(0,len(lista)):
    if x == 0 or x == len(lista) -1:
        print(f'Mi canción Top {x+1} es: {lista[x]}')

print('\n')
diccionario = {'Polera':'Azul','Poleron':'Café','Pantalones':'Azúl','Calcetines':'Blancos'}
index = 0
print("Mi outfit es el siguiente:\n")
for x in diccionario:
    index+=1
    print(f'{index}.- {x} de color: {diccionario[x]}\n')