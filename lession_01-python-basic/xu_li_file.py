def tong_cac_so_trong_file():
    with open("so_nguyen.txt", "r") as r:
        a = 0
        for i in r:
            a += int(i)
    return a
def sao_chep():
    with open(input("Nhap ten file can copy: "), "r") as f:
        noidung = f.read() #noidung: sao chep noi dung trong f ra code (bắt buộc)
    with open(input("Nhap ten file can past: "), "w") as h:
        h.write(noidung)
def chep_bang_cuu_chuong(tu,den):
    chuoi = ""
    while tu <= den:
        i = 1
        chuoi += "Bang cuu chuong thu " + str(tu) + "\n"
        while i <= 10:
            chuoi += str(tu) + " x " + str(i) + " = " + str(tu*i) + "\n"
            i += 1
        tu += 1
    with open("file_bangcuuchuong.txt", "w") as f:
        f.write(chuoi)
while True:
    a = int(input("Nhap a = "))
    if a == 1:
        print(tong_cac_so_trong_file())
        print("System completed")
    elif a == 2:
        try:
            sao_chep()
        except FileNotFoundError:
            print("File not exit")
    elif a == 3:
        tu = int(input("Nhap tu: "))
        den = int(input("Nhap den: "))
        chep_bang_cuu_chuong(tu,den)