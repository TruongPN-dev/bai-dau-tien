#vẽ tam giác cân
while True:
	a = int(input('Nhap so tang a: '))
	for i in range(a):
		print('  '* (a-i) + '* '* (i + i + 1))
	for i in range(a):
		print('* '*(i + 1))
		if (i + 1) == a:
			for j in range(a):
				print('* '* i)
				i = i - 1
	for i in range(a):
		print('  '* (a-i-1) + '* '*(i + 1))
		if (i + 1) == a:
			for j in range(a):
				print('  '* (a - i) + '* '*i)
				i = i - 1