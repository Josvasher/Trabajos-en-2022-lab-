#Programa para poner un texto y contar un caracter en especifico 
n1=str(input("Ingrese el texto a revisar: "))
n2=str(input("Caracter a contar: "))

x=n1.count(n2)
print("Se repite:", x, "veces")
