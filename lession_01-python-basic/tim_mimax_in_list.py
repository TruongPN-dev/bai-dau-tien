lst = []
a = int(input("Nhap vao do dai chuoi: "))
i = 0
while i < a:
    lst.append(int(input(("Vi tri thu " + str(i) + " la: "))))
    i += 1
i = lst[0]
print("List =",lst)
for j in lst:
    if j > i:
        i = j
print("Max la:",i)
i = lst[0]
for j in lst:
    if j < i:
        i = j
print("Min la:", i)