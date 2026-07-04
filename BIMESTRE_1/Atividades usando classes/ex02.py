class Pais:
    def __init__(self):
        self.pais = ''
        self.populacao = 0
        self.area = 0
    def densidade(self): return self.populacao / self.area
    def dicionario(self): return {self.pais : self.densidade()}
    
#desempacotando:
lista_de_paises = []
lista_de_densidade = []
for i in range(10):
    p = Pais()
    p.pais = input('Nome: ')
    p.populacao = float(input('População: '))
    p.area = float(input('Área: '))
    lista_de_paises.append(p.dicionario())

for item in lista_de_paises:
    for i in item:
        lista_de_densidade.append(item[i])

maximo = max(lista_de_densidade)

for item in lista_de_paises:
    for i in item:
        if item[i] == maximo:
            print(f'{i} tem a maior densidade demográfica com: {maximo} hab/km²')