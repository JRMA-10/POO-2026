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

x = input().strip().split(); x = list(map(lambda x: int(x), x))
folhas = 0
primeira = x[0]
segunda = x[1]
total = x[2]

while folhas != total: 
    segundos = 1

    if primeira % segundos == 0: folhas += 1
    if segunda % segundos == 0: folhas += 1

    segundos += 1
print(segundos)