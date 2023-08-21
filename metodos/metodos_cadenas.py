cadena1 = "Hola maquinola"
cadena2 = "sdfs"

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

