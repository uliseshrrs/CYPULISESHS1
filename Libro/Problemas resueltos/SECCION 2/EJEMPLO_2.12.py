SUE= float(input("Ingresa el sueldo del trabajador:"))
CAT= int(input("Ingresa tu categoría:"))
HE = int(input("Ingresa las horas extras trabajadas:"))
if CAT==1:
 PHE=30
elif HE>30:
 NSUE=SUE+30*PHE
elif CAT==2:
 PHE=38
elif CAT==3:
 PHE==50
elif CAT==4:
  PHE=70
else:
  PHE=0
if HE>30:
   NSUE=SUE+30*PHE
else:
    NSUE=SUE+HE*PHE
print(f"Tu sueldo es de:{NSUE}")
print ("Fin del programa")
