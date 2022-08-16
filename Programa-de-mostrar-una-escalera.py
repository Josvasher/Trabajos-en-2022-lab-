#aqui pidiremos el numero de espalones queremos guardandolo e una variable 

n=int(input("ingrese un numero de escalones que quiere"))

#aqui crearemos un ciclo que diga que es de 0 a tantos numeros especificamos en la variable asi repitiendo un for
for i in range (0, n):

  #aqui lo que hace que por cada linea que este se le sume una mas empezando desde 0 hasta las lineas que digamos , y luego lo muestre y luego de eso en vez de hacerlo en diferentes lineas con el "end=""" hacemos que se muestre en una sola linea y luego de eso pasar a la siguente hacendo una vez mas solo que son un caracter mas y asi hasta terminar el for anteior
  for n in range (0,i+1):
    print("# ", end="")
  print()
