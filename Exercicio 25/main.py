N = int(input())

vet = list(map(int, input().split()))

maior = vet[0]

for i in range(1, N):
  if vet[i] > maior:
    maior = vet[i]

maior+=1
assassinatos = [0] * maior

for i in range(maior):
  assassinatos[i] = False

for i in range(N):
  assassinatos[vet[i]] = True;

for i in range(maior):
  if assassinatos[i] == True:
    print(i, end=" ")