def read_last(lines, file):
    if lines < 0:
        return('Введите положительное число строк')
    with open (file, encoding = 'UTF-8') as file:
        import collections
        d = collections.deque(maxlen = lines)
        for line in file:
            d.append(line)
        return list(d)
