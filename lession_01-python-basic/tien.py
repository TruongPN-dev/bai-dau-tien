tien = [500,1000,2000,5000,10000,20000,50000,100000,200000,500000]
while True:
    a = int(input("Nhập số tiền cần đổi: "))
    du = 0
    i = 0
    while i <= 9 and a >= tien[i]:
        j = i - 1
        du = a % tien[i]
        print("Số tờ " + str(tien[i]) + " là " + str(int(a//tien[i])) + " tờ", end="")
        while j >= 0 and du > 0:
            if du >= tien[j]:
                print(", tờ " + str(tien[j]) + " là " + str(int(du//tien[j])) + " tờ", end="")
                du = du - du//tien[j]*tien[j]
            j -= 1
        print()
        i += 1