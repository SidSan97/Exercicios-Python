while(1):
  P, S = input().split()
  S = int(S)

  if(P != '#'):
    if S < 90:
      print(str(P) + " Internar")
    else:
      print(str(P) + " Alta")

  elif(P == '#'):
    break;
