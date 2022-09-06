print("respuestas correctas: ")
RC = int( input())
print("respuestas incorrectas: ")
RI = int( input())
print("respuestas en blanco: ")
RB = int( input())
PCR = RC*3
PRI = RI*-1
PRB = RB*0

PF = PCR + PRI + PRB

print("El puntaje total es:", PF)