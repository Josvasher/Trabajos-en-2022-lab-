#este programa es para saber si un programa es un palindromo pero en un bucle 
print("----------|Ejercicio.5|----------")
fin=str("No")
res=str("No")
si=str("Si")
no=("No")
while fin == res:
  n1=str(input("Ingresar la palabra: "))
  n4=n1.lower()
  n2=''.join(reversed(n1))
  n3=n2.lower()
  print(" ")
  if n4 == n3: 
    print("La palabra que ingreso si es un palindromo")
  else:
    print("No es un polindromo")
  for i in range(0,3):
      print(" ")
  res=input("Quieres terminar el ejercicio? Si. No. ")
  while res != no and res != si: 
    print(" Ingrese una opcion correcta")
    for i in range(0,3):
      print(" ")
    res=input("Quieres terminar el ejercicio? Si. No. ")
    if res == si:
      break 
  if res == no:
    print("----------|Vuelve a hacer el ejercicio|----------")
    for i in range(0,3):
      print(" ")
