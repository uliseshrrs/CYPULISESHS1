# ARREGLOS
# LECTURA
#ESCRITURA / ASIGNACIÒN
#ACTUALIZACION : INTERSERCION, ELIMINACION, MODIFICACIÒN
#ORDENAMIENTO
#BUSQUEDA

#ESCRITURA
frutas = ["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]
# lectura, el selector [ indice ]
print(frutas[2])
#LECTURA CON FOR
#FOR OPSION 1
for indice in range (0,7,1):
    print(frutas[indice])
    print("------")
#for opsion 2 -- por un iterador for each
          
for fr in frutas:
    print(fr)

# ASIGNACION
frutas[2] = "Melon"
print(frutas)
#insercion al final
frutas.append("Naranja")
print(frutas)
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)
# eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2]="limon"
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)


#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda
print(f"La uva esta en la pos.{frutas.index('Uva')}")
print(f"El limon esta en la pos.{frutas.count('Limon')} veces en la lista")

#concatenar
print(frutas)
otras_frutas = ["Rambutan","Mispero","Liche","Pitahaya"]
frutas.extend(otras_frutas)
print(frutas)

#copiar
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
                  

