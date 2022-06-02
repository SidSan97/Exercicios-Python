N = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
d = list(map(int, input().split()))
s = [0] * N
aux = 0

for i in range(N):
  s[i] = u[i] + v[i]

for i in range(N):
  if d[i] == s[i]:
    aux+=1

if aux == N:
  print("OK")
else:
  print("NOPE :(")