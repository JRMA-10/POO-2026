n1, n2, n3, n4, soma = int(input()), int(input()), int(input()), int(input()), 0
for c in (n1, n2, n3, n4): 
    if c % 2 == 0: soma += c
print(soma)