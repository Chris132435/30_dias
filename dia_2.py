#dias 2:30 dias de programacion en python
nombre = "christian"
apellido = "carbajal"
nombre_com = "christian cristobal carbajal garcia"
pais = "México"
ciudad = 23
edad = 28
is_marrier = False
is_true = True
is_ling_on = True
mama, hermano, papa = "guillermina", "jonathan", "tomas"
print(type(nombre))
print(type(apellido))
print(type(nombre_com))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(is_marrier))
print(type(is_true))
print(type(is_ling_on))
print(type(mama))
print(type(hermano))
print(type(papa))

print(len(nombre))
print(len(apellido))
print(len(nombre_com))
if len(nombre) > len(apellido):
    print("nombre")
else:
    print("apellido")
    
num_one = 5
num_tow = 4
total= num_one + num_tow
diff= num_one - num_tow
producto= num_one * num_tow
division = num_one / num_tow
residuo = num_one % num_tow
exp = num_one ** num_tow
print(total)
print(diff)
print(producto)
print(division)
print(residuo) #division de modulo, esta me da el residuo de la divison, por ejemplo 20/5 me da 0, pero 20/3 me da 2 
print(num_one // num_tow) #division entera, esta me da el resultado de la division sin decimales, por ejemplo 20/5 me da 4, pero 20/3 me da 6.666666666666667
print(exp) 

def circulo():
    print("calcularemos el area de un circulo, recuerda que r esta en metros [m]")
    radio = input("introdusca el radio: ")
    pi = float(3.141592)
    area = pi * (int(radio)**2)
    
    perimetro = 2* pi *int(radio)
    
    print("el area es: ", area, "m^2")
    print("el perimetro es: ", perimetro, "m")
    

    
def datos_personales():
    nombre2 = input("nombre: ")
    apellido2 = input("apellido: ")
    pais2 = input("pais: ")
    edad2 = input("edad: ")
    datos_personales = {
        "nombre": nombre2,
        "apellido": apellido2,
        "pais": pais2,
        "edad": edad2,
    }
    print("tus datos son: ", list(datos_personales.values())) #usamos ".values()" para obtener los valores del diccionarios, es decir los datos de las variables que introducimos en el diccionario
    
    
    
help("keywords")
