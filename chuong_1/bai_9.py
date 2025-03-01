import math
x = int(input("Nhập x: "))
f = round(math.log(x,4) + math.log(2,x),2)
print("Giá trị của biểu thức là: ""{:.2f}".format(f))