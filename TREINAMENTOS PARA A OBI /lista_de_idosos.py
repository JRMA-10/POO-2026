n = int(input()); idades = list(map(lambda x: int(x), input().strip().split()))
if len(idades) != n: raise ValueError
ordem_idosos = sorted(filter(lambda x: x >= 60, idades)); ordem_idosos.reverse()
numero_de_idosos = [range(len(ordem_idosos))]