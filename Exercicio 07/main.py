L1,P1 = input().split()
L2,P2 = input().split()
L3,P3 = input().split()

L1 = int(L1)
L2 = int(L2)
L3 = int(L3)

P1 = int(P1)
P2 = int(P2)
P3 = int(P3)

L = L1 + L2 + L3 
P = P1 + P2 + P3

if(L > P):
  print("Lucas")
elif(P > L):
  print("Pedro")
else:
  print("Empate")