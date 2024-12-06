def bang_cuu_chuong(tu, den):   
    chuoi = ""
    while tu <= den:
        i = 1
        chuoi += "Bang cuu chuong thu " + str(tu) + "\n"
        while i <= 10:
            chuoi += str(tu) + " x " + str(i) + " = " + str(tu*i) + "\n"
            i += 1
        tu += 1
    return chuoi
def dem_so(tu,den):
    chuoi = ""
    while tu <= den:
        if tu != den:
            chuoi += str(tu) + ", "
        else:
            chuoi += str(tu)
        tu += 1
    return chuoi
def in_3_so_chan(tu,den):
    chuoi = ""
    dem = 0
    while tu <= den:
        if tu % 2 == 0:
            if tu != den:
                chuoi += str(tu) + ", "
                dem += 1
                if dem == 3:
                    chuoi += "\n"
                    dem = 0
            else:
                chuoi += str(tu)
        tu += 1
    return chuoi
def in_3_so_le(tu,den):
    chuoi = ""
    dem = 1
    while tu <= den:
        if tu % 2 != 0:
            if den % 2 == 0:
                if tu != (den - 1) and dem != 3:
                    chuoi += str(tu) + ", "
                    dem += 1
                else:
                    chuoi += str(tu) + "\n"
                    dem = 1
            else:
                if tu != den and dem != 3:
                    chuoi += str(tu) + ", "
                    dem += 1
                else:
                    chuoi += str(tu) + "\n"
                    dem = 1
        tu += 1
    return chuoi
def menu():
    while True:
        print("1. Bang cuu chuong")
        print("2. Dem so")
        print("3. In so chan")
        print("4. In so le")
        print("5. Thoat chuong trinh")
        a = int(input("Ban can tinh gi: "))
        if a == 1:
            print("Bang cuu chuong")
            tu = int(input("Tu: "))
            den = int(input("Den: "))
            print(bang_cuu_chuong(tu,den))
        elif a == 2:
            print("Dem so bat dau")
            tu = int(input("Tu: "))
            den = int(input("Den: "))
            print(dem_so(tu,den))
        elif a == 3:
            print("In so chan bat dau")
            tu = int(input("Tu: "))
            den = int(input("Den: "))
            print(in_3_so_chan(tu,den))
        elif a == 4:
            print("In so le bat dau")
            tu = int(input("Tu: "))
            den = int(input("Den: "))
            print(in_3_so_le(tu,den))
        elif a == 5:
            break
        else:
            print("Nhap sai, moi nhap lai")
menu()