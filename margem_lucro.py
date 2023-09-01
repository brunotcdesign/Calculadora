

produto = int (input("valor produto: "))
custo = int (input("custo de produçao: "))
despesas = int (input("despesas mensais: "))

margem_lucro = ((produto - (custo + despesas)) / produto) * 100

print(margem_lucro)