print("Ejemplos de tuplas")
canciones=("Te_amo", "El NoNoa", "amor eterno")
print(canciones)

y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)