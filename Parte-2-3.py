n1=str(input("Ingrese el primer nombre "))
n2=str(input("Ingrese el segundo nombre "))
a1=str(input("Ingrese el primer apellido "))
a2=str(input("Ingrese el segundo  apellido "))
#guarde cada variable 
p1=(n1[0])
p2=(n2[0])
#Espeficamos que solo necesitamos el primer elemento de la variable
p3="@baco.com"

t=p1+p2+"."+a1+a2+p3
#agrupamos todo junto para unirlos
p=t.lower()
#ponemos todo en minusculas para que se vea mas estetico
print(p)
#lo mostramos 
