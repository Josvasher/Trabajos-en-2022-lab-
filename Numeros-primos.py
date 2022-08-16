#este problema dira si el numero que pongan es primo o no 
n=int(input("Ingrese un numero ")) #solicitamos un numero

contador=1
divisores=0

while contador<=n:
  residuo=n%contador
  print(residuo)
  if residuo == 0:
    divisores=divisores+1
  contador=contador+1
if divisores==2:
  print ("no es primo")
  print("Tiene ",divisores, " divisores")
else:
  print("es primo")
  print("Tiene ",divisores, " divisores")
