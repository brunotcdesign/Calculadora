#custo por tatuagem


maquina = int(input("Valor do maquinário: "))

material = int(input("Custo mensal: "))

salario = int(input("Salario planejado:  "))

valor_hora = float(input("Valor da hora: "))

horas_trabalhadas = float(input("Media de horas trabalhadas no mês: "))

estudio = int(input("Porcentagem do Estudio: "))

maquina_custo = float(maquina / 60)
despesa = float(valor_hora * (estudio / 100))

custo_tatuagem = ((maquina_custo + material + salario ) / horas_trabalhadas) + despesa

print ("Custo da hora: ", "{:.2f}".format (custo_tatuagem))

margem_lucro = float(((valor_hora - (custo_tatuagem)) / valor_hora) * 100)

print("sua margem de lucro é: ", "{:.2f}".format(margem_lucro))

print("Uma margem de lucro saudável para serviços deve ser de 20% segundo dados do SEBRAE.")

input()