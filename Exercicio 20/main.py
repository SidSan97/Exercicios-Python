A = int(input())
l = list(map(int, input().split()))
C = int(input())

achou = 0

for i in range(A):
  if(l[i] == C):
    achou = 1
    break

if(achou == 1):
  print(C)
else:
  print(-1)