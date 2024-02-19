#creamos un conjunto con set

conjunto = frozenset(set(['dato1']))  #convertimos a conjuntos los elementos de una lista y luego lo convertimos en un
conjunto2 = {'datoX'}

print(type(conjunto))  #imprime <class 'set'>
print(type(conjunto2))  #imprime <class 'set'> Ambos son conjuntos

#Metiendo un conjunto dentro de otro conjunto

conjunto3 = {conjunto, 'dato3', 'dato4'} #puedo agregar a conjunto porque esta frozenset y los otros datos  no lo estan pero son parte del conjunto el cual NO se puede modificar.

print(conjunto3)

conjunto1 = {1,3,5,7,-19}
conjunto2 = {1,7,3}

resltado = conjunto2.issubset(conjunto1)   #Devuelve True si el primer conjunto esta completamente en el segundo o False si no lo esta
resultado = conjunto2 <= conjunto1
print(resultado)   #Imprimirá True si todos los elementos de conjunto2 están en conjunto

resltado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
print(resultado)

#para verificar si hay un numero en comun

resultado = conjunto2.isdisjoint(conjunto1) #Devuelve True o False dependiendo de si hay algun elemento común entre ambos conj

print(conjunto1.intersection(conjunto2)) #Imprime los numeros que estan en ambos conjuntos