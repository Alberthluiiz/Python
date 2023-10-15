### STRINGS ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string)) 

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String  \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\t Este es un String con tabulación"
print(my_tab_string)

my_scape_string = "\t Este es un String \n escapado"
print(my_scape_string)

# FORMATEO

name, surname, age = "Luis", "Guillén", 22

print("Mi nombre es {} {} y mi edad es {} años".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s años" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age) + " años")
print(f"Mi nombre es {name} {surname} y mi edad es {age} años")

# DESEMPAQUETADO DE CARACTERES 

language = "python"
a, b,c ,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#   DIVISIÓN

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

#   REVERSE 

reversed_language = language[::-1]
print(reversed_language)

#   FUNCIONES
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith('Py'))
print(language.startswith('py'))
print("Py" == "py")