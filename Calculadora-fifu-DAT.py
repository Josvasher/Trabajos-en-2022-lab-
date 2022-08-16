#este programa es una calculadora de formulas simples de fisica fundamental 
eje=int(input("Ingrese el ejercicio que quiere: 1. Calcular Distancia 2. Calcular velocidad 3. Calcular tiempo "))

if eje == 1:
  print("---Ejercicio-#1---")
  v=float(input("Ingrese la velocidad en m/s "))
  t=float(input("Ingrese el tiempo en Segundos "))
  d=float(v*t)
  print("La distancia es de ", d,"m ")
          
elif eje == 2:
  print("---Ejercicio-#2---")
  d=float(input("Ingrese la distancia en m"))
  t=float(input("Ingese el tiempo en Segundos"))
  a=float(d/t)
  print("La aceleracion es de", a,"m/s")
elif eje == 3:
  print("---Ejercicio-#3---")
  d=float(input("Ingrese la distancia en m"))
  v=float(input("Ingrese la velocidad en m/s "))
  t=float(d/v)
  print("El tiempo sera de", t,"segundos")

else: 
  print("no ha ingresado una opcion correcta ")
