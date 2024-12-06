l1 = [2,4,3]
l2 = [9,4,2,5,9,7,2,3,9]
l3 = []
ghi = 0
nho = 0
i = 0
while True:
    ghi = l1[i] + l2[i] + nho
    nho = 0
    if ghi > 10:
        nho = ghi // 10
        ghi = ghi % 10
    elif ghi == 10:
        ghi = 0
        nho = 1
    l3.append(ghi)
    i += 1
    if i >= len(l1) or i >= len(l2):
        break
while True:
    if len(l1) < len(l2):
        ghi = l2[i] + nho
        nho = 0
        if ghi > 10:
            nho = ghi // 10
            ghi = ghi % 10
        elif ghi == 10:
            ghi = 0
            nho = 1
        l3.append(ghi)
        i += 1
        if i >= len(l2):
            break
    elif len(l1) > len(l2):
        ghi = l1[i] + nho
        nho = 0
        if ghi > 10:
            nho = ghi // 10
            ghi = ghi % 10
        elif ghi == 10:
            ghi = 0
            nho = 1
        l3.append(ghi)
        i += 1
        if i >= len(l1):
            break
    else:
        break
if nho == 1:
    l3.append(1)
print(l3)