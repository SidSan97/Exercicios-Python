A,D,P = input().split()

A = int(A)
D = int(D)
P = int(P)

TOTAL = (A + D + P) / 110 * 100
TOTAL = int(TOTAL)

if(TOTAL <= 50):
  print("Seu pokemon nao fara progresso em batalhas")
  
elif(TOTAL >= 51 and TOTAL <= 66):
  print("Seu pokemon esta acima da media")
  
elif(TOTAL >= 67 and TOTAL <= 79):
  print("Seu pokemon certamente me chamou atencao")

elif(TOTAL >= 80 and TOTAL <= 100):
  print("Seu pokemon e uma maravilha")
  
else:
  print("Hum, parece que houve um erro")