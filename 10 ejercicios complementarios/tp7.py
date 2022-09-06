print("Ingrese los lados: ")
b = float(input("B: "))
c = float( input("C: "))

print("Ingrese el ángulo en grados sexagesimales:")
alfa = float( input())

a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*PI/180 ) )**0.50

print("El lado a es:", a)