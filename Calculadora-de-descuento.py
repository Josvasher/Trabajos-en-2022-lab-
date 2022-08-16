#este programa ayuda a dar el descuento despues de una compra 
Pro=float(input("Ingrese la cantidad de huevos que compra "))
pre=float(input("Ingrese el precio del producto"))
if Pro > 5 : 
  print("Se te aplicara el descueto del 40% por la compra de mas de 5 huevos")
  Des=0.40
  Desca= pre*Des
  Prefie= Desca*Pro 
  Prefia= Pro*pre
  print(Prefie, "Q Descuento")
  print(Prefia, "Q Precio sin descuento")
  print("Descuento aplicado", Prefia-Prefie, "Q")
else:
  Prefia= Pro*pre
  print(Prefia, "Q Precio sin descuento")

  
