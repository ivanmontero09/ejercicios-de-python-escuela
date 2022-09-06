print("escribe cantidad de GB: ")
GB= float(input())

MB= GB*1024
MD= GB/1.44

print("convertido a mb es: ", MB)
print("convertido a md es : ", math.ceil(MD))