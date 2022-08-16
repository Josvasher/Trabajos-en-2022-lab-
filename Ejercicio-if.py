#este programa dice si un numero es Weird o no 

a=2 
n=int(input())

b= n%2

if b == 0 and 1<n<6  : 
  print("Not Weird")
if b == 0 and 5<n<21:
  print("Weird")
if b == 0 and n<20:
  print("Not Weird")
if b == 0:
  print("Not Weird")
else: 
  print("Weird")
