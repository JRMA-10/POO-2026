class Agua: 
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0
    def calculo(self):
        primeiro = 10
        terceiro = self.consumo - 20
        if self.consumo > 10:
            if self.consumo - primeiro > 10:
                valor = 38 + (5 * 10) + (6 * terceiro)
            else: 
                valor = 38 + (5 * (self.consumo - primeiro))
        else:
            valor = 38
        return valor
    
p1 = Agua()
p1.mes = int(input('Mês: '))
p1.ano = int(input('Ano: '))
p1.consumo = float(input('Consumo do mês: '))
calculo_final = p1.calculo()

print(f'A conta do mês {p1.mes} deu R$ {calculo_final:.2f}')