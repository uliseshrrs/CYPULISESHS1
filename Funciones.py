def sumar (x , y):
    z = x + y
    return z
def restar (x, y):
    return x - y
    
def mi_print (texto):
    print(f"Este es mi print: {texto}")
def multiplica (valor , veces):
    if veces == None :
        print("Debes de emviar el segundo argumento de la funcion")
    else :
        print( valor * veces)
def comanda (mesa , comensal , entrada , medio , fuerte , postre ="gel de limon"):
    print(f" Mesa {mesa}comensal{comensal}")
    print(f"\t Entrada : {entrada}")
    print(f"\t segundo tiempo: {medio}")
    print(f"\t plato fuerte: {fuerte}")
    print(f"\t postre:{postre}")
    
def comanda2 ( **comida):
  # print(comida)
  llaves = comida.keys()
  for elem in llaves:
      print(elem,"->", comida[elem])
               
def imprime_argumentos (*argumentos):
   # print('------',argumentos,'<-----')
   for index in range(len(argumentos)):
       print(argumentos[index])
a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es  {c}")
c =restar (a,b)
print(f"La resta de esto  {a} y  {b} es  {c}")
mi_print("Hola!!")
multiplica(10 , 3) 
multiplica(10, None)
multiplica('Hola',3)
comanda(2,1, "Ensalada","Sopa de rana","Filete de pompi de sirena","Flan")
comanda("Ensalada","Sopa de rana","Filete de pompi de sirena","Flan", 2,1)
comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de pompi de sirena",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416, 1000, {'ID':'sc01', 'nombre': 'juan'})
imprime_argumentos()
comanda2(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de pompi de sirena",mesa=2,comensal=1 ,postre="strudle de manzana", bebida='coca ligth')
