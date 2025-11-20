def unique(spisok):
    return len(set(spisok))

def common(s1,s2):
    S = set(s1) & set(s2)
    S = list(S)
    S.sort()
    return S
