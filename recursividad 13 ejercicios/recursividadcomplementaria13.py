print ("Ingrese los empleados:")
empleados = int( input())
i = 1
sueldom = 0
print("Ingrese los sueldos: ")
while i <= empleados :
	sueldo = float( input("Ingrese sueldo {0}: ".format(i)))
	if sueldo > sueldom :
		sueldom = sueldo
		c = i
	i = i + 1

print ("El empleado numero ", c, "tiene el mayor sueldo que es:", smayor)