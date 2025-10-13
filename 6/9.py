s = input()

chet = 0
nechet = 0
for i in s:
    if int(i)%2 == 0:
        chet += 1
    else:
        nechet += 1

print(chet, nechet)
