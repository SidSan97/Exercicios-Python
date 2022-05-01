N = input()

N = int(N)
H = 0
M = 0

i = 0

for i in range(N):
  S = input()
  S = int(S)

  if S == 1:
    H+=1
  elif S == 2:
    M+=1

print(H)
print(M)
    