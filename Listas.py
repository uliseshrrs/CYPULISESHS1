#listas
lluvias_norte=[80,60,120,100,70,150,100,47,95,70,100,130]# Cada espacio representa el mes

for indice in range(0,12,1):  #Representa el rango 
    print(f" mes { indice+1 } en region norte={ lluvias_norte[indice]}")
    
print(lluvias_norte[4])# Imprime en pantalla de la variable lluvia_norte
print(lluvias_norte[:5:])

sueldos = []
suma = 0
for indice in range (7):
    sueldos.append(int(input("sueldo:")))
print(sueldos)

for indice in range(7):
     suma+=sueldos[indice]
pomedio = suma / 7
print("El promedio de sueldos es{promedio}")
cont = 0
for indice in range (7):
    if sueldos [indice]> promedio:
        cont +=1
        print(f"Arriva:{sueldos[indice] }")
