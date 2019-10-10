#print tiene 4 formas de uso
"""
1 .- con comas
2 .- con signo '+'
3 .- con la funcion format ()
4 .- Es con una variable de format()
"""
#con comas , concatenar agregando
#un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print (edad , estatura , nombre )
# con '+'  hace lo mismo pero no hace el casting automatico
# realiza el casting automatico
# no agrega espacio
print ( str (edad) + str (estatura) + nombre)
# 3.- funcion format ()
print ("Nombre: () Edad: (0)".format (nombre, edad, estatura))
# 4.- con una variante de format () simplificada
print (f"Nombre: \(nombre)\ \nEdad:\t(edad)")

print("solo hay 10 tipos de personas,las que saben binario y las que no", end="---"
print ("otra linea")   

        
       

