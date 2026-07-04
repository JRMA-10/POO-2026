from datetime import datetime
from enum import Enum

class Pagamento(Enum): 
    EM_ABERTO = 1
    PAGO_PARCIAL = 2 
    PAGO = 3

class Boleto: 
    def __init__(self, cod, emissao, venc, valor): 
        # atributos que vão ser validados
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # atributos com valor inicial pré-definido
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        #supondo que o código de barras deve ter 10 dígitos
        if len(cod) != 10: raise ValueError('Código deve ter 10 dígitos')
        self.__cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError('Data não pode ser no futuro!')
        self.__data_vencimento = emissao
    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError('Data não pode ser no futuro!')
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError
        self.__valor_boleto = valor
    def pagar(self, valor_pago):
        #substituiu: set_valor_pago, set_data_de_pagamento e set_situacao_de_pagamento
        if valor_pago < 0: raise ValueError('Valor pago não pode ter um valor negativo! ')
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError('Boleto já foi pago!')
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_boleto == self.__valor_pago: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_valor(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_pago
    def get_data_pagamento(self): return self.__data_pagamento
    #está com esse nome no diagrama
    def get_situacao(self): return self.__situacao_pagamento
    def __str__(self):
        s = f'Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}'
        s += f'Valor: R$ {self.__valor_boleto:.2f} - Valor Pago: {self.__valor_pago:.2f}'
        s += f'Data de Pagamento: {self.__data_pagamento}'
        s += f'Situação: {self.__situacao_pagamento}'
        return s

class BoletoUI:
    boletos = []
    def main(): 
        escolha = 0
        while escolha != 10:
            escolha = BoletoUI.menu()
            match escolha: 
                case 1: BoletoUI.inserir()
                case 2: BoletoUI.listar()
                case 3: BoletoUI.atualizar()
                case 4: BoletoUI.excluir()
                case 5: BoletoUI.BoletosEmAberto()
                case 6: BoletoUI.BoletosPagos()
                case 7: BoletoUI.BoletosAVencer()
                case 8: BoletoUI.BoletosVencidos()
                case 9: BoletoUI.PagarBoletos()
    def menu(): 
        print('[1] INSERIR \n[2] LISTAR \n[3] ATUALIZAR \n[4] EXCLUIR \n[5] VISUALIZAR BOLETOS EM ABERTO \n[6] VISUALIZAR BOLETOS PAGOS \n[7] VISUALIZAR BOLETOS A VENCER \n[8] VISUALIZAR BOLETOS VENCIDOS \n[9] PAGAR BOLETOS')
        return int(input('Informe a sua escolha: '))
    @classmethod
    def inserir(cls):
        codigoBarras = input('Informe o código de barras: ').strip()
        dataEmissao = datetime.strptime(input('Informe a data de emissão: \n', '%d/%m/%Y')).split()
        dataVencimento = datetime.strptime(input('Informe a data de vencimento: \n', '%d/%m/%Y')).split()
        valorBoleto = int(input('Informe o valor do Boleto: '))
        boleto = Boleto(codigoBarras, dataEmissao, dataVencimento, valorBoleto)
        cls.boletos.append(boleto)
    @classmethod
    def listar(cls):
        for i in cls.boletos: print(i)
    @classmethod
    def atualizar(cls):
        BoletoUI.listar()
        codBarras = input('Informe o código de Barras: ').split()
        for i in cls.boletos: 
            if i.get_cod_barras == codBarras: 
                dataEmissao = i.set_data_emissao(datetime.strptime(input('Informe a data de emissão: \n', '%d/%m/%Y')).split())
                dataVencimento = datetime.strptime(input('Informe a data de vencimento: \n', '%d/%m/%Y')).split()
                valorBoleto = int(input('Informe o valor do Boleto: '))
    def excluir():
        pass
    def BoletosEmAberto():
        pass
    def BoletosPagos(): 
        pass
    def BoletosAVencer():
        pass
    def BoletosVencidos():
        pass
    def PagarBoletos():
        pass