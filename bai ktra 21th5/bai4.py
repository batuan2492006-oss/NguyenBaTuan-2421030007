a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
s = a + b
print("Tong =", s)
solonnhat = 0
i = s
while i > 0:
    so = i % 10
    if so > solonnhat:
        solonnhat = so
    i = i // 10
print("Chu so lon nhat =", solonnhat)