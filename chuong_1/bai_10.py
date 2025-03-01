import math
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
tu = math.sin(x)
mau = ((2*x + y) / math.cos(x)) + (x**y / (x-y))
f = tu / mau
print("{}".format(f))

