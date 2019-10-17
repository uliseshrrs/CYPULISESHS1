COMPRA = float (input("Ingresa el prrcio del producto:"))
if COMPRA <500:
    PAGAR = (COMPRA)
else:
    if COMPRA<=1000:
      PAGAR=(COMPRA-COMPRA*0.05)
    else:
        if COMPRA <=7000:
         PAGAR=(COMPRA-COMPRA*0.11)
        else:
            if COMPRA<=15000:
             PAGAR=(COMPRA-COMPRA*0.18)
            else:
                  PAGAR=(COMPRA-COMPRA*0.25)
print(f"El nuevo precio del producto con el descuento ya aplicado es de:${PAGAR}$")
