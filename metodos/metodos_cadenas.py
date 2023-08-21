cadena1 = "Hola maquinola"
cadena2 = "sdfs"
cadena3 = "Hola,Como,Estas?"
dir(cadena2)
#con el metodo dir() me muestra todos los metodos que puedo utilizar con lo que coloque dentro de los parentesis.

#Los metodos se trabajan asi:  resultado = cadena1.upper()  //similar a JS

resultado = cadena1.upper()  #upper() me pasa toda la cadena a mayuscula.
resultado = cadena1.lower()  #lower() me pasa toda la cadena a minuscula.
resultado = cadena1.capitalize()  #capitalize() me pasa la primer letra de la cadena a Mayuscula. (OJo!! porque convierte todo a minuscula)
print (resultado)

letra_a_buscar = "lao"
busqueda_find = cadena1.find(letra_a_buscar)
if busqueda_find == -1:
    print("No existe la letra buscada")
else:
    print(f"la letra buscada {letra_a_buscar} esta en la posicion {busqueda_find}")
    
#find() devuelve la posicion de la letra buscada, si coloco un string, solo me busca la primer letra no encuentra, devuelve -1

#! index()  la diferencia es que sino encuentra la letra, nos tira una excepcion. 

es_numerico = cadena2.isnumeric()  #Si es numerico, devuelve true, sino false pero debe estar entre " "

es_alfa = cadena2.isalpha()

if es_numerico:
    print(es_numerico)

#si es alfanumerico devuelve true  PERO solo sino tiene espacios y solo de la A a la Z 
       
print (es_alfa)

# .count() cuenta cuantas veces aparece lo buscado en la cadena de texto y sino lo encuentra aparece 0

buscar_coincidencias = cadena1.count("a")
print (buscar_coincidencias)

#contamos cuantos caracteres tiene la cadena!! Ojo len NO es un metodo es una funcion por lo tanto se coloca  nombre = lent(cadena1)

contar_caracteres = len(cadena2)
print(contar_caracteres)

#Verificamos sin una cadena empieza con otra cadena, si es asi devuelve true
empieza_con = cadena1.startswith("Ho")
print (f" Is True if start with, so is: {empieza_con}")

#Verificamos sin una cadena termina con otra cadena, si es asi devuelve true
termina_con = cadena1.endswith("la")
print(termina_con)

#reemplaza la cadena dada por la cadena nueva .replace()  SINO encuentra coincidencia con la cadena buscada, nos devuelve la cadena inicial.
nueva_cadena = cadena2.replace("sd", "ae")
print(nueva_cadena)

cadena_oredenada = cadena3.replace("," , " ")
print(cadena_oredenada.capitalize())

#el metodo .split(",") me separa y me genera una lista nueva PERO me lo separa cuando le coloco la "," sino NO lo separa 
separada = cadena3.split("*")
print(separada[0])