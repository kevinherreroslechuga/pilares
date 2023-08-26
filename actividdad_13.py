
#importamos libreria 
import statistics
import time



#Programa 1 para conversion de grados

 
#Declaracion e inicializacion de variables
print("Programa para convercion de grados")
fahrenheit= float(input("Ingrese los grados fahrenheit que desea convertir:"))
celsius=float
celsius=(fahrenheit-32)*5/9
print("\n")

#Imprime resultado
print(f"Los grados  fahrenheit: {fahrenheit} convertidos  a Celsius son: {celsius}")
print("\n")
print( "Iniciando el segundo programa")
time.sleep(3)
print("Inicia programa 2.")


#Programa 2 calculos con dos numeros


 
#Declaracion e inicializacion de variables
print("Programa para calculos con dos numeros")
num_1= float(input("Ingrese el primer numero:"))
num_2= float(input("Ingrese el segundo numero:"))
print("\n")

#Imprime resultado
print(f"La suma de sus numeros es: {num_1+num_2}. ")
print(f"La resta de sus numeros es:{num_1-num_2}.")
print(f"La multiplicacion de sus numeros es:{num_1*num_2}")
print(f"La division de sus numeros es:{num_1/num_2}.")
print("\n")


print( "Iniciando el tercer programa")
time.sleep(5)
print("Inicia programa 3.")


#Programa 3 calcula perímetro y área de rectángulo 


#Declaracion e inicializacion de variables
print("Programa para calcular perimetro y area de un rectangulo")
base_rec= float(input("Ingrese la base del rectángulo:"))
altura_rec= float(input("Ingrese la altura del rectángulo:"))

perimetro_rec = 2 * (base_rec + altura_rec)
area_rec = base_rec * altura_rec

#Imprime resultado
print("\n")
print(f"El perímetro del rectángulo es:{perimetro_rec}. ")
print(f"El área del rectángulo es:{area_rec}. ")
print("\n")

print( "Iniciando1 el cuarto programa")
time.sleep(3)
print("Inicia programa 4.")

d
#Programa 4 calcula la media de tres numeros


#Declaracion e inicializacion de variables
print("Programa para calcular la media de tres numeros")
n_1= float(input("Ingrese el primer numero:"))
n_2= float(input("Ingrese el segundo numero:"))
n_3= float(input("Ingrese el tercer numero:"))

media_n=[n_1,n_2,n_3]
print("\n")

print(f"La media de los numeros ingresados es:{statistics.mean(media_n)}. ")
