N = int(input())

vetor1 = list(map(int, input().split()))

for i in range(N-1, -1, -1):
  print(vetor1[i], end=" ") 