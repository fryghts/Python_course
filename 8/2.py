spisok = list(map(int,input().split()))

#max_elem = spisok[0]
#max_idx = 0
#for idx in range(0,len(spisok)):
#    if spisok[idx] > max_elem:
#        max_elem = spisok[idx]
#        max_idx = idx

max_elem = max(spisok)
max_idx = spisok.index(max_elem)
print(f'Значение: {max_elem}, индекс: {max_idx}')
