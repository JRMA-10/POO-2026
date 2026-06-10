n = int(input()); numeros = input().strip().split(); numeros = list(map(lambda x: int(x), numeros))
if len(numeros) != n: raise ValueError
cont = 0
pre = 0
now = 0
lista_de_valores = []

for i in range(len(numeros)):
    now = numeros[i]
    if i == 0: pre = 0
    else: pre = numeros[i - 1]
    if now >= pre:
        cont += 1
    else: 
        lista_de_valores.append(cont)
        cont = 1

print(max(lista_de_valores))