L1 = float(input ("INGRESA EL 1ER LADO DEL TRIANGULO:"))
L2 = float(input ("INGRESA EL 2DO LADO DEL TRIANGULO:"))
L3 = float(input ("INGRESA EL 3ER LADO DEL TRIANGULO:"))
S = (L1 + L2 + L3) / 2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print(f"UN TRIANGULO CON UN LADO {L1} CM, {L2} CM, Y UN LADO {L3} CM Y TIENE UN AREA DE {AREA} CM")   
