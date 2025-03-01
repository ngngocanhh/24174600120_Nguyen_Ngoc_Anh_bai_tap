import math
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
c = int(input("Nhập giá trị c: "))
delta = b**2 - 4*a*c
if delta > 0 :
    print("Phương trình có hai nghiệm phân biệt")
    x1 = (-b + delta ** 1/2) / 2*a
    print("x1 = ",x1)
    x2 = (-b - delta ** 1/2) / 2*a
    print("x2 = ",x2)
elif delta == 0 :
    print("Phương trình có 1 nghiệm")
    x = -b / 2*a
    print("x = ",x)
else :
    print("Phương trình vô nghiệm ")
