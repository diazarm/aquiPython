# funcion para crear una lista list(["aqui", "algo"])

lista = list(["creamos",  "una", "lista", 43])
lista2 = list(["creamos",  "una", "lista", 43])
print(lista)

lista_vacia = list([])  # similar a js  lista = [];
print(lista_vacia)

#para que me devuelva la cantidad de elementos de una lista (asi como .length() en JS ) como ya cree una lista puedo usarlo asi:

cantidad_de_elementos = len(lista)
print(cantidad_de_elementos)

#Agregando elemento a la lista .append("elemento a agregar")  OJO! me lo agrega al final de la lista

lista.append("jajaja")

print(lista)

#Con insert agrego un elemento a la lista en la POsicion que yo quiera (OJO!! AGREGA NO CAMBIA ni elimina)
lista.insert(2, "palabra nueva")
print(lista)

#Agregamos UNA LISTA dentro de la lista (va al final) 
lista.extend(["tuki", 3,4])
print (lista)
print("--------------------------Eliminamos---------------------------------")

#Eliminamos un elemento de la lista, pero debemos decirle el indice pop(0)

lista.pop(2) #seria "palabra nueva"
print(lista) 
#!  si quiero eliminar el ultimo elemento coloco -1 // lista.pop(-1) y elimina el ultimo elemento de la lista.

# para eliminar un elemento por su valor usamos remove("jajaja") 
lista.remove("jajaja")
print(lista)

#Para eliminar TODO! .clear() y me queda la lista vacia
lista2.clear()
print(lista2)

#Sort ordena de forma ascendente pero solamente si es numero o logico, (False, True, 0,1,2,3)

lista_numerica = list([True,34,5,2,56,False])

lista_numerica.sort()
lista_numerica.sort(reverse=True) #con reverse los hacemos descendente


print(lista_numerica)

