while True:
    a = int(input("Nhap so can tim: "))
    i = 1
    dem = 0
    while i <= a:
        if a % i == 0:
            dem += 1
        i += 1
    if dem == 2:
        print(a, "la so nguyen to")
    else:
        print(a, "khong la so nguyen to")
    