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
def tinh_tuoi(nam_sinh):
    chuoi = ""
    tuoi = 2024 - nam_sinh
    if tuoi % 12 == 0:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Thin"
    elif tuoi % 12 == 1:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Meo"
    elif tuoi % 12 == 2:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Dan"
    elif tuoi % 12 == 3:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Suu"
    elif tuoi % 12 == 4:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Ti"
    elif tuoi % 12 == 5:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Hoi"
    elif tuoi % 12 == 6:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Tuat"
    elif tuoi % 12 == 7:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Dau"
    elif tuoi % 12 == 8:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Than"
    elif tuoi % 12 == 9:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Mui"
    elif tuoi % 12 == 10:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Ngo"
    else:
        chuoi += "Ban " + str(tuoi) + " tuoi" + "\n" + "Ban Tuoi Ty"
    return chuoi
def tim_kich_thuoc(loai):
    if loai == "DTHT" or loai == "CVHT":
        ban_kinh = int(input("Nhap ban kinh hinh tron: "))
    else:
        dai = int(input("Nhap chieu dai: "))
        rong = int(input("Nhap chieu rong: "))
    if loai == "CVHCN" or loai == "CVHV":
        return (dai + rong) * 2
    elif loai == "DTHCN" or loai == "DTHV":
        return dai * rong
    elif loai == "DTHT":
        return 3.14159 * ban_kinh
    else:
        return 2 * 3.14159 * ban_kinh
while True:
    q = input("Ban muon tinh gi: ")
    if q == "Bang cuu chuong":
        tu = int(input("Nhap bang cuu chuong can tinh tu: "))
        den = int(input("Nhap bang cuu chuong can tinh den: "))
        print(bang_cuu_chuong(tu, den))
    elif q == "Tinh tuoi":
        nam_sinh = int(input("Nhap nam sinh: "))
        print(tinh_tuoi(nam_sinh))
    elif q == "Tim kich thuoc":
        loai = input("Nhap loai can tinh: ")
        print(tim_kich_thuoc(loai))