import math
x = int(input("Nhập giá trị x: "))
tu = -x + math.sqrt(x**2 + 4)
mau = (x**4 + 1)**1/7
fx = tu / mau
print("Kết quả là:""{}".format(fx))