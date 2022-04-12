N = input()

N = int(N)

if(N < 3):
  C = N / 3 + 1
  C = int(C)

  SUB = N - C
  SUB = int(SUB)

  if(SUB == 1):
    print("Chapeuzinho Vermelho " + str(C))
    print("Vovozinha 1")
    print("Lobo Mau 0")
  elif(SUB == 0):
    print("Chapeuzinho Vermelho " + str(C))
    print("Vovozinha 0")
    print("Lobo Mau 0")
else:
  if(N % 3 == 0):
    D = N / 3
    D = int(D)
  
    print("Chapeuzinho Vermelho " + str(D))
    print("Vovozinha " + str(D))
    print("Lobo Mau " + str(D))
  
  else:
    if(N % 3 != 0):
      C = N/3 + 1
      C = int(C)
    
      SUB = N - C;
      SUB = int(SUB)
  
      if(SUB % 2 == 0):
        DIV = SUB / 2 
        DIV = int(DIV)
        print("Chapeuzinho Vermelho " + str(C))
        print("Vovozinha " + str(DIV))
        print("Lobo Mau " + str(DIV))
      else:
        V = SUB / 2 + 1
        V = int(V)
        L = SUB / 2
        L = int(L)
        print("Chapeuzinho Vermelho " + str(C))
        print("Vovozinha " + str(V))
        print("Lobo Mau " + str(L))