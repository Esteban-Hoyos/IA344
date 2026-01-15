#Librerías
import re 


#Codigo 
print ("Librería cargada correctamente")

#Ejemplo1
texto="Mi número es 12345"
Resultado=re.search(r"\d+",texto)
print(Resultado.group())


