#estre programa pide todo lo que se necesita para calcular el area de un terreno que esta dentro de un bucle
pre=1 
def area (x,y):
    x=float(input("Cual es el ancho de la figura?: "))
    y=float(input("Cual es la altura de la figura?: "))
    res=x*y
    print("El area es de: ", res)


  
while pre == 1:
   area(1,2)
   for i in range(0,3):
    print(" ")
   pre=int(input("Quiere continuar? Si. 1, No. 2 "))
   if pre == 2:
      break
   elif pre == 1: 
      pre= 1
   for i in range(0,3):
      print(" ")
   else:
    print("Ingrese una opcion correcta ")
    pre=int(input("Quiere continuar? Si. 1, No. 2 "))
   
  
  
  









