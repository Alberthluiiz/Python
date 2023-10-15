print('============');
print(' Conversor  ');
print('============\n');

print('Menú de opciones: \n');
print('1.- Convertir de número a palabra.');
print('2.- Convertir de palabra a número. \n');

opcion = int(input('Seleccione una opción entre 1 al 2: '));

if opcion == 1:
    print('\n================================');
    print(' Conversor de Número a Palabra  ');
    print('==============================\n');

    opcionUno = int(input('Digite un número: '));
    if opcionUno == 1:
        print('El número ingresado es Uno');
    elif opcionUno == 2:
        print('El número ingresado es Dos');
    elif opcionUno == 3:
        print('El número ingresado es Tres');
    elif opcionUno == 4:
        print('El número ingresado es Cuatro');
    elif opcionUno == 5:
        print('El número ingresado es Cinco');
    else:
        print('El número ingresado no esta registrado');
    print('Realizado por: Luis Guillén');
elif opcion == 2:
    print('\n================================');
    print(' Conversor de Palabra a Número  ');
    print('==============================\n');

    opcionDos = input('Digite la palabra del número que desee: ');
    opcionDos = opcionDos.lower();

    if opcionDos == 'uno':
        print('El número ingresado es "1"');
    elif opcionDos == 'dos':
        print('El número ingresado es "2"');
    elif opcionDos == 'tres':
        print('El número ingresado es "3"');
    elif opcionDos == 'cuatro':
        print('El número ingresado es "4"');
    elif opcionDos == 'cinco':
        print('El número ingresado es "5"');
    else:
        print('El número ingresado no esta registrado');
    print('Realizado por: Luis Guillén');
else:
    print('Opción no valida');


