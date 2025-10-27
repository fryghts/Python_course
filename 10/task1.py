def divides(a,b):
    if (a == 0) or (b == 0):
        return 0
    if a%b == 0:
        return a//b
    elif b%a == 0:
        return b//a
    else:
        return 0
    
print(divides(4,0))
