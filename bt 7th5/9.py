
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
s = a + b + c
tong = str(s)
chan = 0
for chuso in tong:
    if int(chuso) % 2 == 0:
        chan += 1
print(f"Tổng (a + b + c) = {tong}")
print(f"Số lượng chữ số chẵn trong tổng là: {chan}")