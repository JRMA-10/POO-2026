class Pais:
    def __init__(self, pais, populacao, tamanho):
        self.pais = pais
        self.populacao = populacao
        self.tamanho = tamanho
    def conta(self):
        return self.populacao / self.tamanho

pais = input('Digite o País: ')
populacao = int(input('Digite a população: '))
tamanho = int(input('Digite a área em Km²: '))
c1 = Pais(pais, populacao, tamanho).conta()
print(f'A densidade demográfica do {pais} é igual a {c1:.2f} Hab/km²')