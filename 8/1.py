spisok = list(map(int, input().split(',')))

#for elem in spisok[::2]:
#   print(elem)

for idx in range(0,len(spisok),2):
    print(spisok[idx])
print()

for elem in spisok:
    if elem % 2 == 0:
        print(elem)

print()
for idx in range(0,len(spisok)-1):
    if spisok[idx] < spisok[idx+1]:
        print(spisok[idx+1])
