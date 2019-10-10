edad = int (input("DAME TU EDADA:"))
INE = bool (int (input ("TIENES INE (0 NO / 1 SI)?:")))
if edad >= 18 and INE == True:
    print("ES MAYOR DE EDAD")
    print("PUEDE ENTRAR AL BAR")
else:
    print ("ERES MENOR DE EDAD")
    print ("PUEDES IR AJUGAR LOL")
    print ("FIN DEL PROGRAMA")
