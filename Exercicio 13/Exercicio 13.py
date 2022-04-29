N = int(input())

if N % 2 == 0 and N <= 10000:
  print("S")
  print("S")
elif N % 2 == 0 and N > 10000:
  print("S")
  print("N") 
elif N % 2 != 0 and N > 10000:
  print("N")
  print("N")
elif N % 2 != 0 and N <= 10000:
  print("N")
  print("S")