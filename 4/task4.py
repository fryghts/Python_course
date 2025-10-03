A = int(input('Введите число: '))
B = int(input('Введите число: '))
if A <= B:
    S = A
    while S <= B:
        print(S)
        S += 1
else:
    S = A
    while S >= B:
        print(S)
        S -= 1
