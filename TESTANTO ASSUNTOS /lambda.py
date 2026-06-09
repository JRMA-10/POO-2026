minha_funcao = [(1, 2), (1, 3), (1, 1)]

print(sorted(minha_funcao, key = lambda x: x[1])) #no sorted, podemos usar uma key para ditar a ordem dos elementos. O x assume um valor de cada elemento dentro da função

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x ** 2, dados ))) # No map, usa-se primeiro a operação e depois a lista com os dados

vamos = map(lambda x: x * 2, dados)
print(list(vamos))