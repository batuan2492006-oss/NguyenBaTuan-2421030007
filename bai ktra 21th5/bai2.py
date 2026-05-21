n = int(input("Nhap n: "))
s = 0
i = n
while i > 0:
    chu_so = i % 10
    s += chu_so
    i = i // 10
print("Tong cac chu so =", s)
if s % 3 == 0:
    print("Tong chia het cho 3")
else:
    print("Tong khong chia het cho 3")