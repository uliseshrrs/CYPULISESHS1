MAT = int(input("INGRSA LA MATRICULA DEL ALUMNO:"))
CAL1 = float (input("INGRESA LA PRIMERA CALIFICACIÓN:"))
CAL2 = float (input("INGRESA LA SEGUNDA CALIFICACIÓN:"))
CAL3 = float (input("INGRESA LA TERCERA CALIFICACIÓN:"))
CAL4 = float (input("INGRESA LA CUARTA CALIFICACIÓN:"))
CAL5 = float (input("INGRESA LA QUINTA CALIFICACIÓN:"))
PRO = (CAL1+CAL2+CAL3+CAL4+CAL5) /5
if PRO >=6:
   print(f"EL ALUMNO CON LA MATRICULA: {MAT} HA APROVADO!, SU CALIFICACIÓN ES:{PRO}")
else :
    print(f"EL ALUMNO CON LA MATRICULA: {MAT} HA REPROBADO!, SU CALIFICACIÓN ES:{PRO}")
    print("FIN DEL PROGRAMA")
