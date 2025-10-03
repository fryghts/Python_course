c_max = c_min = int(input())

while c := int(input()):
    if c > c_max:
        c_max = c
    if c < c_min:
        c_min = c

print(c_max, c_min)
