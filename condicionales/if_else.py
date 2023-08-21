edad = 6

if edad >35:
    print("deberias estar en tu casa")
elif edad >= 18: 
    print("podes pasar")
else: 
    print(f"No podes pasar tenes {edad} anios") 
    
#Primero va la condicion mayor, luego utilizo elif (que seria else if) sino.. else

# el if anidado trabaja mucho con la identacion.

sueldo = 550
gasto = 700

if sueldo >= 1500: 
    print("estas bien pa!")
    if sueldo - gasto < 0 :
        print("estas gastando demasiado")
    else: print("estas bien")
elif sueldo <1500 : 
    if sueldo >500 & sueldo <1500 :
        print("ganas bien para latam")
    else:
        print("ganas muy poco")

