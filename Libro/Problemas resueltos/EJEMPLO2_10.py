A = int (input("Ingrsa el valor A:"))
B = int (input("Ingrsa el valor B:"))
C = int (input("Ingrsa el valor C:"))
if A > B:
    if A > C :
        print(f"A  es mayor con valor a {A}")
    elif A == C :
        print(f" A y C son iguales a {A} y son lo9s mayores")
    else:
        print(f"C que vale {C} es el mayor")
elif A == B :
     if A > C:
         print(f"A y B son los mayores con valor {B}")
     elif A == C:
         print(f"B es mayor {B}")
     else:    
         print(f"C que vale {C} es el mayor")
elif B > C:
    print(f"B que vale {B} es el mayor")
elif B == C:
    print(f"B Y C son los mayores con valor {B}")
else:
    print(f"C es el mayor con valor {C}")
    print("FIN DEL PROGRAMA!!")
