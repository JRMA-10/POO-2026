n = input('Digite um texto: ').strip()
lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
soma = 0
for c in n:
    if c in lista:
        num = int(c)
        soma += num
print(soma)