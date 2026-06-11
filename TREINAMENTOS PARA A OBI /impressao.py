'''''
Xt e Yt
TOTAL

Xt * T = TOTAL 
Yt * T = TOTAL

2 * x = 30 
5 * x = 30
x = 15 
x' = 6

max(x, y)
Quando o tempo é y, quantos folhas já temos? 
'''

primeira, segunda, total = map(int, input().split()); folhas, segundos = 0, 1
while folhas != total: 
    if segundos % primeira == 0: folhas += 1
    if segundos % segunda == 0: folhas += 1
    if folhas >= total: break
    segundos += 1
print(segundos)
