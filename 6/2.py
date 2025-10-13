#1 + 1*2 + 1*2*3 + 1*2*3*4 + ...
N = int(input())
P = 1
Z = 0
for i in range(1,N+1):
    P *= i
    Z += P
print(P)
print(Z)
