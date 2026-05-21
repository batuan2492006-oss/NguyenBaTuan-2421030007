m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
s = 0
i = n
while i > 0:
    so = i % 10
    s += so
    i = i // 10
print("Tong cac chu so cua n =", s)
if s != 0 and m % s == 0:
    print(m, "chia het cho", s)
else:
    print(m, "khong chia het cho", s)