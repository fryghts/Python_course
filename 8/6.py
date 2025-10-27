spisok = input().split(',')
counters = [0 for _ in range(len(spisok))]

while (stroka := input()) != '.':
    stroka = stroka.split()
    for i in range(len(spisok)):
        counters[i] += stroka.count(spisok[i])

print(*spisok)
print(*counters)
