sinonims = dict()
while text:=input():
    a,b = text.split()
    sinonims[a] = b
    sinonims[b] = a

print(sinonims)
    
