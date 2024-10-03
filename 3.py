# De esa misma lista que aparezca un mensaje Estoy cursando <materia>, donde <materia> es cada una de las de la lista  .
# Definición de la lista de materias
print ("Martinez Tagle Luis Angel 3w Este programa muestra si va a cursar alguna materia") #imprime el nombre del programador
materias = [
    "Matemáticas",
    "Historia",
    "Ciencias",
    "Literatura",
    "Educación Física",
    "Biología",
    "Química",
    "Física",
    "Arte",
    "Música"
]

      # Función para generar mensajes sobre las materias
def mostrar_materias(materias):
    print("Lista de materias que estoy cursando:\n") #imprime lo que quiere decir el texto 
    for materia in materias: 
                 # Generar el mensaje para cada materia
        mensaje = (f"Estoy cursando {materia}.")
        print(mensaje)  # Mostrar el mensaje en pantalla

# Llamar a la función para mostrar las materias
mostrar_materias(materias)
