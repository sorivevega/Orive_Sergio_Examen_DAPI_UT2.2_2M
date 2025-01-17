def OrdenarLista():
    Lista = ['1', '4', '2', '5', '3']
    '''
    Lo que he hecho aqui a sido crear una funcion con el normbre OrdenarLista.
    Hacemos una lista con numeros desordenados-
    Primero abrimos el fichero en el que se va a escribir la lista con el comando 'with open () as file.
    Lo abrimos asi para no tener que preocuparnos de cerrarlo ya que una vez se termine de ejecutar el codigo se cerrara solo.
    Esta lista se escribira en el fichero 'ListaOrdenada.txt' pero primero usamos el comando .sort, para ordenarlo.
    Como se ordena de menor a mayor, usamos el comando .reverse para que este ordenado de mayor a menor.
    Una vez este ordenada, lo escribimos en el fichero.
    '''
    with open('ListaOrdenada.txt', 'w') as file:
        Lista.sort()
        Lista.reverse()
        file.write(Lista)


def NumeroPar():
    Num = ['1', '2', '3', '4', '5', '6']
    '''
    Lo que he hecho aqui a sido crear una funcion con el nombre NumeroPar.
    Dentro de esta funcion hacemos una lista de numeros ordenador.
    Abrimos un fichero con nombre 'ListaNumeros.txt' con el comando 'with open() as file.
    Esto lo hacemos asi para que no tengamos que cerrarlo manualmente nosotros y que se cierre una vez se termine el codigo.
    Despues escribimos la lista de numeros dentro del fichero.

    Despues creamos una condicion para que si los numeros que estan dentro de la lista 'Num' que a su vez
    esta dentro de file son pares, se debera abrir un segundo fichero con nombre 'ListaDePares.txt' y escribir ahi los numeros pares de la lista.
    Este fichero tambien lo abrimos con el comando 'with open() as file.
    '''
    with open('ListaNumeros.txt', 'w') as file:
        file.write(Num)

    if Num in file % 2 == 0:
        with open('ListaDePares.txt', 'w') as file:
            file.write(Num)
            