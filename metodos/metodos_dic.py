# keys() devuelve las claves // get() devuelve el valor de una clave // clear() elimina todos los elementos // pop() elimina un elemento // items() para iterar el diccionario

diccionario = {
    "nombre" : "marcelo",
    "apellido" : "Diaz",
    "subs": 10000
}

claves = diccionario.keys()
#el metodo keys() me muestra la key del diccionario. (tambien nos sirve para iterar)

print(claves)

claves_get = diccionario.get("nombre")
#get() lo que hace es devolver el valor de la clave que le especifique.

print(claves_get)
#Otra forma de utilizar similar al get() es colocarle diccionario[0] entonces toma el valor de la clave que esta en la posicion 0
#si no encuenta lo que le pido en get("fdsf") el programa me devuelve none, que es similar a undefined.

#.pop("apellido")  elimina clave valor de lo que le coloque.
diccionario.pop("apellido")

print(diccionario)

#!diccionario.clear() #borra todo y deja solo {}

#.items()devuelve un elemento pero Iterable

diccionario_iterable = diccionario.items()
print(diccionario_iterable)
