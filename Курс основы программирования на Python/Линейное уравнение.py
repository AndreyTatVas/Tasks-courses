a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

x = (d * e - f * b) / (d * a - b * c)
y = (f * a - e * c) / (d * a - b * c)

print('{:.6} {:.6}'.format(x, y))
