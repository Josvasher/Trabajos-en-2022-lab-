#este programa sirve para saber si una palabra es un palindromo o no 
n1=str(input("Ingresar la palabra: "))
n4=n1.lower()
n2=''.join(reversed(n1))
n3=n2.lower()
print(" ")
if n4 == n3: 
 print("La palabra que ingreso si es un palindromo")
else:
  print("No es un polindromo")
