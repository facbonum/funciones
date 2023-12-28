def miFuncion():
    print('Mi primera función!')

# miFuncion()

""" def imprimeDato(argumentoUno):
    print('Mi argumento es', argumentoUno)

imprimeDato('parametro 12') """

""" def imprimeDato(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

# imprimeDato('Chanchito') # TypeError: imprimeDato() missing 1 required positional argument: 'apellido'

imprimeDato('Chanchito', 'Feliz') # El nombre completo es: Chanchito Feliz """

def imprimeDato(*nombre): # argumento variable
    print('El nombre completo es:', nombre[2])

# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')

""" def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre='Chanchito', apellido='Feliz')

 """

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

# miFuncion2('Batman')
# miFuncion2()

def miFuncionLista(lista): # pass a list as an argument
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)
'''
Si nosotros ejecutamos esto, 
(llamando esta función solamente, por ejemplo: 
concatenaNombres(['Chanchito', 'Feliz']) )
no pasa absolutamente nada y es porque 
los valores cuando nosotros los retornamos, tenemos que necesariamente 
capturarlos en otra variable.

Así es que cuando nosotros llamemos a esta función, voy a indicar acá 
una nueva variable que se va a llamar nombres.
'''

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)