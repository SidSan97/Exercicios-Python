N = input()
N = int(N)
igual = 0
soma = 1

if(N == 1):
  print("Dattebayo")
  quit()

for i in range(1, int(N / 2) + 1):
  soma = soma * 2
  
  if soma == N:
    igual+=1
    break;

if(igual == 0):
  print("Tururuuu")
else:
  print("Dattebayo")