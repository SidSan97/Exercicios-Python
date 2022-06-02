S, N = input().split()
S = int(S)
N = int(N)

vetor = [0] * N

for i in range(S):
  P = int(input())
  j = 0
  while j < N:
    vetor[j] = 1
    j+=P

for i in range(N):
  print(vetor[i], end=" ")