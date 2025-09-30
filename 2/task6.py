S = int(input('Введите кол-во секунд с начала суток: '))

H = S//3600
M = (S%3600)//60
C = S%60

print(str(H).zfill(2),':', str(M).zfill(2)
      , ':', str(C).zfill(2), sep = '')
