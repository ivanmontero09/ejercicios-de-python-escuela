print("partidos ganados: ")
pg= int(input())
print("partidos empatados: ")
pe= int(input())
print("partidos perdidos: ")
pp= int(input())

ppg= int(pg*3)
ppe= int(pe*1)
ppp= int(pp*0)

pf= int(ppg+ppe+ppp)
print("puntos totales: ", ppg+ppe+ppp)