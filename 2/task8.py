# y = a1*x + b1
# y = a2*x + b2

# 0 = x(a1-a2) + b1 - b2
# x = (b2 - b1) / (a1 - a2)

a1 = int(input('Введите a1:'))
b1 = int(input('Введите b1:'))
a2 = int(input('Введите a2:'))
b2 = int(input('Введите b2:'))

x = (b2 - b1) / (a1 - a2)
y = a1*x + b1
print('Точка пересечения:',x,y)
