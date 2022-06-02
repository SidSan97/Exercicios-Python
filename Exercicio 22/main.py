N = int(input())
vet = list(map(int, input().split()))
  
for i in range(N):
  if vet[i] % 2 == 0:
    print(vet[i], end = " ")

print()

for i in range(N):
  if vet[i] % 2 != 0:
    print(vet[i], end = " ")
  