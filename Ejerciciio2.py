print('1) Añadir alumno')
print('2) Numero de aprobados')
print('3) Mostrar todo el alumnado')

menu = input('Seleccione una opcion: ')
Base = {}

while menu != 4:

    if menu == '1':
        print('Usted a seleccionado: Añadir Alumno')
        nombre = input('Introduzca el nombre del Alumno: ')
        nota =  float(input('Introduzca la nota del alumno: '))
        Nota = {'nota': nota}
        Base[nombre] = Nota
        print('El alumno ha sido añadido con exito')

    if menu == '2':
        print('Usted a seleccionado: Numero de Aprobados')
        if nota >= 5:
            print ('El numero de aprobados es', len(Base))
        

    if menu == '3':
        print('Usted a seleccionado: Mostrar todo el alumnado')
        print(Base)

    
    menu = input('Seleccione una opcion: ')