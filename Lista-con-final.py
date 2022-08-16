#este programa crea una lista y luego la muestra usando el while 
n1=str(input("Ingrese objetos a la lista "))
lista=[]
n2="Fin"
while n1 != n2:
  n1=str(input("siga ingresando objetos. Si quiere terminar la lista escriba Fin: "))
  lista.append(n1)
lista.pop(-1)
print("Su lista es:",lista)
