PREBAS = float (input("INGRGRESA EL COSTO DEL ARTICULO:"))
if PREBAS >500:
  IMP= 20*0.30 + (PREBAS -40)* 0.50
else:
    if PREBAS >40:
       IMP= 20*  0.30 + (PREBAS -40)*0.40
    else:
        if PREBAS >20:
         IMP=PREBAS-20*0.30
        else:
             IMP=0
PRETOT=PREBAS+IMP
print(f"EL PRECIO DEL ARTICULO ES : {PREBAS} Y EL TOTAL ES {PRETOT}")

