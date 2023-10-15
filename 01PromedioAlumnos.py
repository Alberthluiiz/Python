print('Sisteman para calcular el promedio de un alumno');
print();

nombre = input('¿Cual es tu nombre?: ');
print();

mate = float(input(nombre + ' Cual es tu nota en matematicas: '));
quimica = float(input(nombre + ' Cual es tu nota en quimica: '));
biologia = float(input(nombre + ' Cual es tu nota en biologia: '));
print();

promedio = (mate + quimica + biologia)/3;

if promedio >= 6:
    print('Felicidades ' + nombre + ' Aprobaste con un promedio de: ', promedio);
    print('Felicidades ' + nombre + ' Aprobaste con un promedio de: ', round(promedio,2));
else:
    print('Lo sentimos ' + nombre + ' has "Reprobado" tu nota fue: ', promedio);
    print('Lo sentimos ' + nombre + ' has "Reprobado" tu nota fue: ', round(promedio,1));
print('Fin');