N = int(input())
vetor = list(map(int, input().split()))
soma = 0

for i in range(N):
  soma += vetor[i]

print(soma)