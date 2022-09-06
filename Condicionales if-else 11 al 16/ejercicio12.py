sueldo=float(input(" ingrese el sueldo "))

if sueldo<1000:
	aumento=sueldo*15/100
	sueldo=sueldo+aumento

print(" el sueldo con aumento seria: ", sueldo)