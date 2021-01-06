#   Entrada de dados
N = int(input())

visualizacoes = []
for i in range(N):
    A = int(input())
    visualizacoes.append(A)

# processamento
total = 0
resposta = -1
for i, v in enumerate(visualizacoes):
    dia = i + 1
    total = total + v
    if total >= 1000000 and resposta == -1:
        resposta = dia

# Saida do programa.
print(resposta)
