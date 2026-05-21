n = int(input("Nhap n: "))
s = 0
i = 0
for i in range(n):
    x = float(input(f"Nhap x[{i}]: "))
    if x > 0 and x < 1000:
        s += x
        i += 1
if i > 0:
    tbc = s / i
    print("Trung binh cong =", tbc)
else:
    print("Khong co phan tu thoa man")