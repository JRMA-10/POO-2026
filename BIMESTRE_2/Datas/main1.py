from datetime import datetime # módulo / classe

d = datetime.strptime(input('Informe uma data: '), "%d/%m/%Y")
print(d)
print(d.strftime("%d/%m/%Y"))
#strptime - passa de string para date -- método estático - chama uma classe 
#strftime - passa de date para string - método de instancia - chama uma variavel da class (objeto)

#Método estático e método de instancia 