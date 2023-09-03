import math

def calcular_tamanho_amostra(N, erro_percentual):
    erro_decimal = erro_percentual / 100  # Converter o erro percentual em decimal
    tamanho_amostra = N / (1 + N * erro_decimal**2)
    return math.ceil(tamanho_amostra)  # Arredondar para cima para o tamanho da amostra inteiro mais próximo

# Exemplo de uso
N = 150000  # Tamanho da população total
erro_percentual = 3  # Erro máximo permitido em porcentagem

tamanho_amostra = calcular_tamanho_amostra(N, erro_percentual)
print(f"Tamanho da amostra necessário: {tamanho_amostra}")