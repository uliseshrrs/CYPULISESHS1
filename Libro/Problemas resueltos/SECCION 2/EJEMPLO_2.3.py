import math
#PROGRAMA DE ECUACIÓN CUADRANTICA
A = float(input("INGRESA EL VALOR A:"))
B = float(input("INGRESA EL VALOR B:"))
C = float(input("INGRESA EL VALOR C:"))
DIS = (B*B)-4*A*C
if DIS >= 0:
          X1 =(-B+math.sqrt(DIS))/(2*A)
          X2 =(-B-math.sqrt(DIS))/(2*A)
          print(f"LAS RAICES DE X1 ES: {X1} Y DE X2 ES:{X2}")
print("FIN DEL PROGRAMA")          
