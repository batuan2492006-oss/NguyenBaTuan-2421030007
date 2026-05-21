n = int(input("Nhập n: "))
dem = 0
i = 2
while n > 1:
    if n % i != 0:
        i = i + 1
    else:
        dem = dem + 1
        while n % i == 0:
        n = n // i
print()
print("Số các số nguyên tố là: ", dem)
