#este ejercicio dira si los nombres empiezan o terminan con la misma letra 
print("Los nombres sin mayus solamente con minusculas ")
a=str(input("Ingrese el primer nombre: "))
b=str(input("Ingrese el segundo nombre: "))
if a[-1] == b[-1] or a[0] == b[0]:
  print("Hay concidencia ")
else:
  print("No hay concidencia ")
