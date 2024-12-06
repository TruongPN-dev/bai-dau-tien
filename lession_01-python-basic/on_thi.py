import math
def tinh_phuong_trinh_bac_1():
    chuoi = ""
    a = int(input("Nhap a = "))
    b = int(input("Nhap b = "))
    if a == 0:
        chuoi += "Phuong trinh vo nghiem"
    else:
        if b % a == 0:
            x = int(-b/a)
        else:
            x = round(-b / a, 2)
        chuoi += "Ket qua x = " + str(x)
    return chuoi
def tinh_tong_n():
    n = int(input("Nhap so nguyen duong: "))
    i = 0
    while n > 0:
        i = i + n*n
        n -= 1
    return i
def tinh_phuong_trinh_bac2():
    a = int(input("Nhap tham so a = "))
    b = int(input("Nhap tham so b = "))
    c = int(input("Nhap tham so c = "))
    delta = 0
    chuoi = ""
    if a == 0:
        chuoi += "Error"
    else:
        if a + b + c == 0:
            x1 = 1
            x2 = c/a
        elif a - b + c == 0:
            x1 = -1
            x2 = -c/a
        else:
            delta = b*b - 4*a*c
            if delta < 0:
                return "Phuong trinh vo nghiem"
            elif delta == 0:
                return "x1 = x2 = " + str((-b/2*a))
            else:
                delta = math.sqrt(delta)
                x1 = (-b + delta)/(2*a)
                x2 = (-b - delta)/(2*a)
        chuoi +="x1 = " + str(x1) + "\n" + "x2 = " + str(x2)
    return chuoi
while True:
    print("1: Giai phuong trinh bac 1",
          "2: Giai phuong trinh bac 2",
          "Tinh tong binh phuong cua n so nguyen")
    a = int(input("Nhap can tinh: "))
    if a == 1:
        print("Phuong trinh bac 1 co dang la ax + b = 0")
        print(tinh_phuong_trinh_bac_1())
    elif a == 2:
        print("Phuong trinh bac 2 co dang ax^2 + bx + c = 0")
        print(tinh_phuong_trinh_bac2())
    elif a == 3:
        print(tinh_tong_n())
    else:
        print("Nhap sai, moi nhap lai")