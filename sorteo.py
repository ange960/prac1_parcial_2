#Haz uno que pregunte los numero triunfadores de la lotería , y llene una lista que se va a mostrar en pantalla de menor a mayor.
print("Martinez Tagle Luis Angel 3w Este es un programa que realizara un sorteo de numeros e imprimirá el ganador. ")#imprime la funcion del programa
print("")#imprime espacio en blanco 

numeros=[] # Almacena los numeros ganadores

#Pide al usuario ingresar los numeros de la loteria.(en caso de ser 6.)
numeros.append(int(input("Número 1.- ")))
numeros.append(int(input("Número 2.- ")))
numeros.append(int(input("Número 3.- ")))
numeros.append(int(input("Número 4.- ")))
numeros.append(int(input("Número 5.- ")))
numeros.append(int(input("Número 6.- ")))

numeros.sort()#ordena la lista en forma ascendente
                                    
print("Números ganadores ordenados:", numeros)   #muestra los numeros ganadores