def capitalize(a):
    b = list(a)
    if 'a'<=b[0]<='z' or 'а'<=b[0]<='я':
        b[0]=chr(ord(b[0])-32)
    elif b[0]=='ё':
        b[0]='Ё'
    return ''.join(b)
