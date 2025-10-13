x,y,z = map(int, input().split(','))
x_min, y_min, z_min = x,y,z
x_max, y_max, z_max = x,y,z

while s := input():
    x,y,z = map(int, s.split(','))
    x_min, y_min, z_min = min(x, x_min),min(y, y_min),min(z, z_min)
    x_max, y_max, z_max = max(x, x_max),max(y, y_max),max(z, z_max)

V = (x_max - x_min)*(y_max - y_min)*(z_max - z_min)
print(V)
