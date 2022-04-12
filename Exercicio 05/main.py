N = input()

N = int(N)

H = int(N / 3600)
M = int((N % 3600) / 60)
S = int((N % 3600) % 60)

print(str(H) + "h " + str(M) + "m " + str(S) + "s")