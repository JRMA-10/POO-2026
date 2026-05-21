from datetime import datetime

class Boleto: 
    def __init__(self, codBarras, dataEmissao, dataVencimento, dataPagto, valorBoleto, valorPago, sitPag): 
        self.set_codBarras(codBarras)
        self.set_dataEmissao(dataEmissao)
        self.set_dataVencimento(dataVencimento)
        self.set_dataPagto(dataPagto)
        self.set_valorBoleto(valorBoleto)
        self.set_valorPago(valorPago)
        self.set_sitPag(sitPag)
        self.pagamento_aceito = False
    def set_codBarras(self, c): 
        if len(c) <= 0: self.__codBarras = c
        else: raise ValueError('Código de Barras inválido!')
    def set_dataEmissao(self, de):
        self.__dataEmissao = de
    def set_dataVencimento(self, dv):
        self.__dataVencimento = dv
    def set_dataPagto(self, dpg):
        self.__dataPagto = dpg
    def set_valorBoleto(self, v):
        if v >= 0: self.__valorBoleto = v
    def set_valorBoleto(self, vb):
        if vb >= 0: self.__valorBoleto = vb 
        else: raise ValueError
    def set_valorPago(self, vp):
        if vp > 0: self.__valorPago = vp
    def set_sitPag(self, sp): self.__sitPag = sp
    def get_codBarras(self): return self.__codBarras
    def get_dataEmissao(self): return self.__dataEmissao
    def get_dataVencimento(self): return self.__dataVencimento
    def get_dataPagto(self): return self.__dataPagto
    def get_valorBoleto(self): return self.__valorBoleto
    def get_valorPago(self): return self.__valorPago
    def get_sitpag(self): return self.__sitPag
    def pagar(self):
        self.pagamento_aceito = True
        return self.__valorBoleto - self.__valorPago
    def situacao(self): 
        if self.pagamento_aceito and self.pagar() != 0: return 'Pago parcial'
        elif not self.pagamento_aceito: return 'Em aberto'
        return 'Pago'
    def __str__(self):
        return f'Código de Barras: {self.get_codBarras()} | Data de emissão: {self.get_dataEmissao().strftime("%d/%m/%Y")} | Data de Vencimento: {self.get_dataVencimento().strftime("%d/%m/%Y")} | Data do Pagamento: {self.get_dataPagto().strftime("%d/%m/%Y")} | Valor a ser Pago: {self.get_valorPago():.2f} | Situação de Pagamento: {self.situacao()}'