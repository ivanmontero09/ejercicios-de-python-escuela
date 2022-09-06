i = 1
c = 0
numEntradas = 10
print("Ingrese", numEntradas, "Números:")
while i <= numEntradas:
	n = int( input("Ingrese número: "))
	if n%2 == 0 :
		c = c + 1

	i = i + 1

print ("En", numEntradas, "números enteros hay", c, "números pares")