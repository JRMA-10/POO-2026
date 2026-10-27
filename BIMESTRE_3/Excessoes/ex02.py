try: 
    a = int(input("Informe um dividendo: "))
    b = int(input("Informe um divisor: "))
    print (a / b)
except ValueError as erro: 
    print(erro)
finally: 
    print('Ok')
print('Fim')