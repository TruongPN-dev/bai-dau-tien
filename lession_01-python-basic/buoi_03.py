tu = int(input("Nhap Tu: "))
den = int(input("Nhap den: "))
while tu <= den:
    print("Bang cuu chuong: ", tu)
    a = 1
    while a < 11:
        print(tu, " x ",a, " = ", tu*a)
        a += 1
    tu += 1