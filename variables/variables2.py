#desempaquetado! sirve para tuplas() y para listas []

datos = ("Lunes", 1, True)

dia, numero, booleano = datos

print(f"el primer datos es {dia}")
print(f"el numero en datos es {datos[1]}")


#!Tengo 3 formas de crear una Tupla ()

# creando con tuple
tupla = tuple(['dato1', 'dato2'])
# creando sin parentesis
otraTupla = 'dato1', 'dato4'
# creando usando un solo dato
unaVezMas = 'unicoDato',

print("La tupla original es: ", tupla)
print(f"otra tupla es {otraTupla}")
print(f"y esta otra? {unaVezMas}")