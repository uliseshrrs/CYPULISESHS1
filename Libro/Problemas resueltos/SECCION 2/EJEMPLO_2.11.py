CLAVE =int(input("Ingresa la clave:"))
NUMMIN = int(input("Ingresa la duración de la llamada de en minutos"))
if CLAVE ==12:
 COST=NUMMIN*2
elif CLAVE ==15:
 COST=NUMMIN*2.2
elif CLAVE ==18:
 COST=NUMMIN*4.5
elif CLAVE ==19:
 COST=NUMMIN*3.5
elif CLAVE >=23:
 COST=NUMMIN*6
elif CLAVE ==29:
 COST=NUMMIN*5
print(f"El costo total de la llamada es de {COST}")
