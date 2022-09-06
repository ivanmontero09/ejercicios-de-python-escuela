cant=int(input(" ingrese la cantidad de numeros"))
contmenor=0
contmayor=0

for i in range(1,cant):
	num=int(input(" ingrese un numero "))
	if num>0:
		contmayor=num
	else:
		if num<0:
			contmenor=num

print ("El número menor es :" ,contmenor)
print ("El número mayor es :", contmayor)

		