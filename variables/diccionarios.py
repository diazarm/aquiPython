# un diccionario es como un json

diccionario = dict(nombre="Juan", edad=30, ciudad="Bogota")
print(diccionario)

# salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogota'}

#creando un diccionario con el metodo fromkeys()

diccionario = dict.fromkeys("abcde") # devuelve {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}\
# para solucionar este  problema se le pasa una tupla vacia a fromkeys(), indicando que los valores no son obligatorios

diccionario = dict.fromkeys(["lunes","martes","miercoles"],"clase") 
#devuelve {'lunes':'clase','martes':'clase','miercoles':'clases'} // O sino pongo clase va none.
print(diccionario)