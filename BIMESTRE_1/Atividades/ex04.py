n = input('Digite valores separados por vírgula: ').strip()
soma = 0
for c in n:
    if c != ',':
        num = int(c)
        soma += num
print(soma)