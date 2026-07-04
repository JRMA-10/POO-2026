from datetime import datetime, Zoneinfo

x = datetime.datetime(2026, 5, 1)
'''print(x)
print(type(x))'''

y = datetime.datetime(2026, 5, 19, 14, 30, 0)
'''print(y)
print(y.day)
print(y.month)
print(y.year)
print(y.hour)
print(y.day)
print(y.minute)
print(y.second)
'''

#Zoneinfo("America/Sao_paulo")

# print(datetime.now()

z = datetime.now()
print(z)
print(z.strftime("%d/%m/%Y, %H:%M:%S"))