n = int(input()); idades = list(map(lambda x: int(x), input().strip().split()))
if len(idades) != n: raise ValueError
ordem_idosos = sorted(filter(lambda x: x >= 60, idades)); ordem_idosos.reverse()
lista_tempos = []
for i in ordem_idosos: 
    contador = 0
    while idades.index(i) != ordem_idosos.index(i):
        anterior = idades[idades.index(i) - 1]
        idades[idades.index(i)] = idades[idades.index(i) - 1]
        idades[idades.index(i) - 1] = idades[idades.index(i)]
        contador += 1
    lista_tempos.append(contador)
print(idades)