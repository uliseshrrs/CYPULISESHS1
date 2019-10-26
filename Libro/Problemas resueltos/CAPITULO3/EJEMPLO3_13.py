ARSU = 0
ARNO = 0
MERSU = 50000
MES = 0
ARCE = 0
for i in range (1,13,1):
    print(f" Mes (i):")
    RNO = int (input("Promedio de lluvias del mes zona norte:"))
    RCE = int (input("Promedio de lluvias del mes zona centro"))
    RSU = int (input("Promedio de lluvias del mes zona sur"))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = i
PRORCE = ARCE / 12
print(f"Promedio region centro:{ PROCE }")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MERSUR}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("La zona con mayor lluvia es la region norte")
    else:
            print("La zona con mayor lluvia es la region sur")
elif ARSE > ARSU:
    print("La region con mayores lluvias es la region centro")
else:
        print("La zona con mayor lluvia es region sur")
print("Fin del programa")        


    
