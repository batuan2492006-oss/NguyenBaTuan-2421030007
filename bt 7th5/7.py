import math
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập x{i+1}: ")))
tong_nt = 0
for x in a:
    if la_so_nguyen_to(x):
        tong_nt += x
print("Tổng các số nguyên tố là:", tong_nt)
if tong_nt > 50 and tong_nt % 2 != 0:
    print("Tổng này là số lẻ và lớn hơn 50.")
else:
    print("Tổng này không thỏa mãn điều kiện (lẻ và > 50).")