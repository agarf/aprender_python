# enttrada de dados.
N = int(input())
V = input().split()

for i in range(len(V)):
    V[i] = int(V[i])

# Processameto
total = 0
for elemento  in V:
    total = total + elemento

# Saida do Programma
print(total)
