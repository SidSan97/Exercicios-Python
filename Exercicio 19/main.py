a, b = input().split()

a = int(a)
b = int(b)

primo = 0
resultado = 0

for i in range(a, b):
  for j in range(2, int(i/2)):
    if(i % j == 0):
      resultado+=1
      break

  if resultado == 0:
    primo+=1
    
  resultado = 0

print(primo)