from enum import Enum 
class Estacao(Enum): 
    VERAO = 1
    OUTONO = 2
    INVERNO = 3
    PRIMAVERA = 4

x = Estacao(4)
print(x == Estacao.PRIMAVERA) 

print(Estacao.VERAO.value)
print(Estacao.VERAO.name)

#Conseguimos comparar valores dentro de um atributo com o nome do atributo
#Consegumos ter acesso ao nome e ao valor


from datetime import datetime
y = datetime(2010, 1, 22, 22, 40, 30)
z = datetime.now()
a = z - y
a = a.days
print(a // 365, 'ANOS', 'E', a % 365 // 30, 'MESES')
