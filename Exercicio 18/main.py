P = 0
LIMITE = 1

T = input()
T = int(T)

while LIMITE != 0:
  LIMITE = input()
  LIMITE = int(LIMITE)

  if LIMITE > T:
    P = LIMITE

if P > T:
  print("ALARME")
else:
  print("O Havai pode dormir tranquilo")
