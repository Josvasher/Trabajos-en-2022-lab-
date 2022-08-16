#este programa da diferentes opciones de ejercicios tipo calsular su edad, luego potencias y sobre si alguien mas es su tocayo 

op=float(input("Ingrese el programa deseado, 1. Conocer su edad 2. Calculadora de potencia 3. Saber si son tocayos "))
if op == 1:
  nom=str(input("Ingrese su nombre "))
  edad=float(input("Ingrese su año de nacimiento "))
  a=2022-edad
  print("Usted", nom, "este año va a tener ", a, " años" )
elif op == 2:
  n1=float(input("Ingrese el primer numero "))
  n2=float(input("Ingrese el segundo numero "))
  n3= n1**n2
  print(n3, "es el resultado del primer numero con la potencia del segundo numero  ")
elif op == 3:
  n1=str(input("Ingrese el primer nombre sin mayusculas "))
  n2=str(input("Ingrese el segundo nombre sin mayusculas "))
  if n1 == n2:
    print("Son tocayos")
  else:
    print("No son tocayos") 




