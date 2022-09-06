num= int(input("ingrese cantidad de numeros ")
cont=0

for i in range(1, num):
	num2=int(input("ingrese un numero: "))
	if num2==0:
		cont=cont+1

print("hay ",cont, " ceros")