Q1, Q2, Q3 = input().split()
E1, E2, E3 = input().split()

Q1 = int(Q1)
Q2 = int(Q2)
Q3 = int(Q3)
E1 = int(E1)
E2 = int(E2)
E3 = int(E3)

total = (Q1 - (E1 * 3)) + (Q2 - (E2 * 3)) + (Q3 - (E3 * 3))

print(total)