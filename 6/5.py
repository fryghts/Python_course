#FN = F(n-2)+F(n-1)
N = int(input())

F_minus2 = 0
F_minus1 = 1

for _ in range(2, N+1):
    FN = F_minus2 + F_minus1
    F_minus2 = F_minus1
    F_minus1 = FN

print(FN)
