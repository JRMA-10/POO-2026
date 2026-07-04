'''b = float(input('Informe a base do triângulo: '))
h = float(input('Informe a altura do triangulo: '))
a = b * h /  2
print(f'A área do triangulo é {a:.2f}')'''

#Com classes 
class BasedoTriangulo:
    def __init__(self, base, altura):
        self.base = base #atributos
        self.altura = altura
    def fazer_o_calculo(self): #método
        return self.base * self.altura / 2
    
t1 = BasedoTriangulo(int(input('Digite a base do triângulo: \n')), int(input('Digite a altura do triângulo: \n'))) #Chama o método __init__
print(t1.fazer_o_calculo())
#t1 é uma referência - alguém que armazena o endereço de um objeto; 
#BasedoTriangulo() cria um objeto (ou instancia) da classe
