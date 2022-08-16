#este programa ordena el numero mas grandes primero 
n1=int(input("Ingrese el primer numero "))
n2=int(input("Ingrese el segundo numero "))
if n1 >> n2: 
  print(n1," ", n2,)
elif n2 >> n1:
  print(n2, " ", n1)
elif n1 == n2:
  print(n1, n2)
