# Tipos de variables 

my_string_variable = 'My String variable';
print(my_string_variable);

my_int_variable = 5;
print(my_int_variable);

my_int_to_str_variable = str(my_int_variable);
print(my_int_to_str_variable);
print(type(my_int_to_str_variable));

my_bool_variable = False;
print(my_bool_variable);

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable);

print(type(print(my_string_variable, str(my_int_variable), my_bool_variable)));

print("Este es el valor de:", my_bool_variable);


# Algunas Funciones del sistema
print(len(my_int_to_str_variable));

print(len(my_string_variable)); # CUENTA CUANTAS LETRAS HAY


# Variables en una sola lìnea.  !Cuidado con abusar de esta sintaxis¡
name, surname, alias, age = "Luis", "Guillén", "AlberthLuiiz", 22;
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es", alias);

# Inputs
name = input('What is your name: ');
age = input('How old are you? ');
print(name);
print(age);
print();

# Cambiamos su tipo
name = 23
age = "Alberth"

print(name, age)

# Forzamos el tipo 
address: str = "Mi dirección";
address = True
address = 5;
address = 1.2
print(type(address))







