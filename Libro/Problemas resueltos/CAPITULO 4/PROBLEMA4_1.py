N = int(input("Ingrese el numero de elementos del arreglo:"))
VEC=[]
if N >= 1 and N <= 500:
    #LOGICA
    for I in range (0, N ,1):
        VEC.append(int(input("Ingresa el valor:")))
    VEC.sort()
    print("Listas de numeros sin repeticiones")
    I = 0
    while I <= N-1:
        print(VEC[I])
        REPET = VEC[I]
        while I<= N-1 and REPET == VEC[I]:
         I+= 1
else:
    print("El numero de arreglos es incorrecto:")
   
    
#TAREA PROBLEMA 4.3 Y LEER DE LA PG 209 A 217
