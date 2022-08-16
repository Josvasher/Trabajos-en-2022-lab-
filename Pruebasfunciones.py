#este codigo es para practicar una funcion que calcula el area de un terreno 

pa="Fin"
hola=""
def area():
  n=int(input("Ingrese el largo del terreno: "))
  n1=int(input("Ingrese el ancho del terreno: "))
  print("el area del terreno es de ",n*n1,"m2")
  

while hola != pa:
  area()
  hola=str(input("Quiere terminar el programa? Si. escriba Fin No. de le enter "))
  print(hola)
   
