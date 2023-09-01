
    

valor = float (input("Valor do produto: "))
frete = float (input("Valor do frete: "))
valorDolar = float(input("Vaor do dolar: "))

valorTotal = valor + frete

if valorTotal > valorDolar * 50:
    valorTotal = valorTotal + (valorTotal * 0.6)
    print ("Valor com imposto de importaçao: ", valorTotal)
    valorTotal = valorTotal + (valorTotal * 0.23)
    print   ("Valor final com ICMS: ", valorTotal)
    
else:
    valorTotal = valorTotal + (valorTotal * 0.23)
    print   ("Valor final com ICMS: ", valorTotal)
    
input()