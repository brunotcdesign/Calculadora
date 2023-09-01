#custo por tatuagem

maquina = int(input("Valor da sua maquina: "))
material = int(input("Gasto de material mensal: "))
salario = int(input("Salario mensal planejado: "))
valor_hora = float(input("Valor hora: "))
estudio = int(input("Porcentagem do Estudio: "))

maquina_custo = float(maquina / 24)
despesa = float(valor_hora * (estudio / 100))

custo_tatuagem = ((maquina_custo + material + salario ) / 44) + despesa

print ("Custo da hora: ", "{:.2f}".format (custo_tatuagem))

margem_lucro = float(((valor_hora - (custo_tatuagem)) / valor_hora) * 100)

print("sua margem de lucro é: ", "{:.2f}".format(margem_lucro))

print("Uma margem de lucro saudável para serviços deve ser de 20% segundo dados do SEBRAE.")

input()