for line in fi:
    n = int (line)
    k = 2
    while n > 1:
        while n % k != 0:
            k = k + 1
        if n % k == 0:
            print (k, file = fo, end = " ")
            while n % k == 0:
                n = n // k