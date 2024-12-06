while True:
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    print("Uoc chung lon nhat la: ",b)