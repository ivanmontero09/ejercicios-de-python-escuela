print("coordenadas A: ")
AX = float(input("Ax: "))
AY = float(input("Ay: "))

print("coordenadas B: ")
BX = float(input("Bx: "))
BY = float(input("By: "))

D = ( (AX-BX)**2 + (AY-BY)**2 )**0.5
print("La distancia:", D)