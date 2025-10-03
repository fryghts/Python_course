'''
year = int(input('Введите год: '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('YES3')
else:
    print('NO3')
'''

x = int(input ('Введите год: '))
if x % 4 != 0:
    print ('NO')
elif x % 100 != 0:
    print ('YES')
elif x % 400 != 0:
    print ('NO')
else:
    print ('YES')

