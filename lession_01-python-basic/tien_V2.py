from collections import Counter
def xac_suat(lst, target, chuoi=[]):
    if sum(chuoi) == target:
        chuoi.sort()
        return [chuoi]
    elif sum(chuoi) > target:
        return []
    ket_qua = []
    for i in range(len(lst)):
        ket_qua += xac_suat(lst, target, chuoi + [lst[i]])
    ket_qua.sort()
    return ket_qua
lst = [1000, 2000 ,5000, 10000, 20000, 50000, 100000, 200000, 500000]
while True:
    target = int(input("Nhập target = "))
    tien = []
    for i in xac_suat(lst,target):
        if i not in tien:
            dem = Counter(i)
            for a, b in dem.items():
                print(" " + str(b) + " tờ " + str(a), end="")
            print()
        tien.append(i)