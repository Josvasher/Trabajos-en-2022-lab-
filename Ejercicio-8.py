#este ejercicio es para ver si la palabra que ingresen empieza con consonante o vocal 
letra=str(input("Ingrese una lectra para saber si es una vocal o consonante "))
if (len(letra)) >> 1:
  print("Ha sobre pasado el lime de letras, porfavor solo ingrese una letra ")
elif (len(letra)) == 1:
  if letra == "a": 
    print("Es una vocal")
  elif letra == "e":
    print("Es una vocal")
  elif letra == "i": 
    print("Es una vocal")
  elif letra == "o":
    print("Es una vocal")
  elif letra == "u":
    print("Es una vocal")
  else: 
    print("Es una consonante")
else: 
  print("no has ingresado una letra correctamente ")
