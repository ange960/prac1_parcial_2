#Haz uno que pregunte los numero triunfadores de la lotería , y llene una lista que se va a mostrar en pantalla de menor a mayor.
print("Martinez Tagle Luis Angel 3w Este es un programa que realizara un sorteo de numeros e imprimirá el ganador

print("") #imprime el espacio en blanco 
print("Este es un programa que imprimirá una lista de materias para luego pedir la calificación obtenida. ")#imprime la funcion del programa
print("") #imprime el espacaio en blanco 


# Almacenar las materias en una lista
materias = ["Matematicas", "lengua", "Inglés", "Ecosistemas", "Formación", "Frameworks"]
print(materias) #se imprime la lista de materias
# Mostrar un mensaje para cada materia en pantalla
for materia in materias:
    print(f"Estoy cursando {materia}.") #imprime elñ texto 
    print(" ") #uimprime el espacio en blaco 
    mat=(float(input("¿Cuál fue la calificación que obtuviste en matematicas?: ")))
    leng=(float(input("¿Cuál fue la calificación que obtuviste en lengua?: ")))
    ing=(float(input("¿Cuál fue la calificación que obtuviste en ingles?: ")))
    eco=(float(input("¿Cuál fue la calificación que obtuviste en ecosistemas?: ")))
    form=(float(input("¿Cuál fue la calificación que obtuviste en formación?: ")))
    frame=(float(input("¿Cuál fue la calificación que obtuviste en frameworks?: ")))
    print("")  #imprime el espacio en blanco 
    print("has obtenido una calificación de ", mat) #imprime la primera calificacion 
    print("has obtenido una calificación de ", leng)
    print("has obtenido una calificación de ", ing) 
    print("has obtenido una calificación de ", eco) 
    print("has obtenido una calificación de ", form) 
    print("has obtenido una calificación de ", frame)
