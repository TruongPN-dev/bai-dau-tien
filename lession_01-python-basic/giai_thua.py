while True:
	a = int(input("Giai thua cua: "))
	i = 1
	b = 1
	while i <= a:
		b = b*i
		if i != a:
			print(str(i) + " x ", end="")
		else:
			print(i, end="")
		i += 1
	print(" =",b)
	if a == "n":
		break