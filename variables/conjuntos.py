#creamos un conjunto con set

conjunto = frozenset(set(['dato1']))  #convertimos a conjuntos los elementos de una lista y luego lo convertimos en un
conjunto2 = {'datoX'}

print(type(conjunto))  #imprime <class 'set'>
print(type(conjunto2))  #imprime <class 'set'> Ambos son conjuntos

#Metiendo un conjunto dentro de otro conjunto

conjunto3 = {conjunto, 'dato3', 'dato4'} #puedo agregar a conjunto porque esta frozenset y los otros datos  no lo estan pero son parte del conjunto el cual NO se puede modificar.

print(conjunto3)
