spisok = list(map(int, input().split()))

max_idx = spisok.index(max(spisok))
min_idx = spisok.index(min(spisok))

spisok[max_idx],spisok[min_idx] = spisok[min_idx], spisok[max_idx]
print(*spisok)
