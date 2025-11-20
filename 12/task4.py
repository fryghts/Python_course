N = int(input())
d = dict()
for _ in range(N):
    text = input()
    eng, rus = text.split('-')
    eng = eng.strip()
    rus = rus.split(',')
    rus = list(map(str.strip, rus))
    for rus_word in rus:
        d.setdefault(rus_word,[]).append(eng)

for rus,eng_list in d.items():
    print(f'{rus} - {", ".join(eng_list)}')

