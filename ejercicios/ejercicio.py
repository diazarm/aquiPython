numero = True
print (type(numero))
#Solamente me va a variar cuando lo trabaje como str, luego vuelve a ser int

print (type(str(numero))) 
print (type(numero))

print("-------------------Ejercicios--------------------------")
# Ejercicio 1: Manipulación de Listas
# Escribe un programa que realice las siguientes operaciones:

# Crea una lista llamada numeros con los números del 1 al 10.
# Imprime la lista original.
# Agrega el número 11 al final de la lista.
# Inserta el número 0 al principio de la lista.
# Imprime la lista después de realizar las operaciones anteriores.
# Elimina el número 5 de la lista.
# Imprime la lista final.

numeros = list(range(1, 11))
print(f"Lista Original: {numeros}")
numeros.append(11)
numeros.insert(0, 0)
print(f"lista con elementos agregados {numeros}")
numeros.remove(5)
print(f"Lista Final: {numeros}\n")


# Ejercicio 2: Manipulación de Tuplas
# Escribe un programa que realice las siguientes operaciones:

# Crea una tupla llamada frutas con al menos 5 nombres de frutas.
# Imprime la tupla original.
# Convierte la tupla a una lista llamada lista_frutas.
# Agrega dos frutas adicionales a lista_frutas.
# Convierte lista_frutas de nuevo a una tupla llamada nuevas_frutas.
# Imprime la tupla nuevas_frutas.

print("-------------------Ejercicios2--------------------------")

frutas = ("manzanas", "peras", "limones", "cantaloupe", "sandia")
print(f"Tupla Original: {frutas}")
lista_frutas = list(frutas)
print(lista_frutas)
lista_frutas.extend(["naranja", "tomate"]) #porque con .extend agrega  varios elementos a la vez
nuevas_frutas = tuple(lista_frutas)
print(f"Lista convertida a Tupla: \n{nuevas_frutas}")


# Ejercicio: Calculadora Simple
# Escribe un programa en Python que realice las siguientes operaciones:

# Pregunta al usuario que ingrese dos números enteros.
# Realiza la suma, resta, multiplicación y división de los dos números.
# Imprime los resultados de cada operación.

print("-------------------Ejercicios3--------------------------")

def sumar(a, b):
    suma = a + b
    return f"La Suma es: {suma}"

def restar(a, b):
    resta = a - b
    return f"La Resta es: {resta}"

def multiplicar(a, b):
    multi = a * b
    return f"La Multiplicación es: {multi}"

def default():
    return "Opción no válida"

def switch_case(case, a, b):
    switch_dict = {
        1: sumar,
        2: restar,
        3: multiplicar
    }
    selected_function = switch_dict.get(case, default)
    return selected_function(a, b)

# Ingreso de datos
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
opcion = int(input("Ingrese una operacion: 1-sumar 2-restar 3-multiplicar "))

# Uso de la función switch_case
resultado = switch_case(opcion, num1, num2)
print(resultado)

