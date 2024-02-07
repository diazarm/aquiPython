#Tenemos las listas y tuplas, las tuplas NO se pueden modificar, la listas si

lista = ["hola", "soy marcelo", False, 1.78]  #las listas van entre [ ]  
tupla = ("hola", "soy marcelo", False, 1.78)  #las tuplas van entre ( )
lista[2] = "nacana"
print (f"Este es tercer el elemento de la tupla {tupla[3]}")

#conjuntos (set) NO puede haber datos duplicados y NO puedo acceder a los elementos, si! al conjunto completo y NO puedo modificar un elemento. va con { }

conjunto = {"hola", "este es el conjunto", False, 1.78}
#se puede recorrer con un bucle
print(conjunto)

#diccionario, es como un objeto de JS (dict)   key : value

diccionario = {
    'nombre' : 'marcelo',
    'apellido' : 'Diaz',
    'esta_emocionado' : True,
    'peso' : 80
    }
print(diccionario['apellido'])

# de aca para abajo es practica

laListaVaConCorchetes = ["Hola","Soy Marcelo"]
print(laListaVaConCorchetes[0])
laListaVaConCorchetes[0] = "cara de mono"
print(laListaVaConCorchetes[0])

laTuplaVaEntreParentesis = ("Chau","Soy Francesco")

print(laTuplaVaEntreParentesis)

elConjuntoEsUnico = {45,"Gato"}
print(elConjuntoEsUnico)

# Ejercicio 1: Manipulación de Listas
# Escribe un programa que realice las siguientes operaciones:

# Crea una lista llamada numeros con los números del 1 al 10.
# Imprime la lista original.
# Agrega el número 11 al final de la lista.
# Inserta el número 0 al principio de la lista.
# Imprime la lista después de realizar las operaciones anteriores.
# Elimina el número 5 de la lista.
# Imprime la lista final.

numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros)
