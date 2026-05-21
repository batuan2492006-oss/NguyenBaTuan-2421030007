n = int(input("Nhap n: "))
z = 1
i = n
while i > 0:
    chu_so = i % 10
    z *= chu_so
    i = i // 10
print("Tich cac chu so =", z)
if z % 2 == 0 and z > 20:
    print("Thoa man dieu kien")
else:
    print("Khong thoa man dieu kien")