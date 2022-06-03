N, M = map(int, input().split())
placa = list(map(int, input().split()))

limitevel = [i for i in placa if i!=0]
print(*limitevel [len(limitevel)- M : len(limitevel)])