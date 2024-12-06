lst = []
l = []
a = int(input("Nhap vao do dai chuoi: "))
i = 0
while i < a:
    lst.append(int(input(("Vi tri thu " + str(i) + " la: "))))
    i += 1
for i in lst:
    if i not in l:
        l.append(i)
    else:
        l.remove(i)
print("List =",lst)
for i in l:
    print("Phan tu xuat hien 1 lan la:",i)