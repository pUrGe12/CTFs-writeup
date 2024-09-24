str1 = []
str2 = 'clnooNKnooN;[AE'
v4 = 0
v5 = 2

while v5 < 15:
	v6 = (v5-1)%5
	if v5-1 == 5*((v5-1)//5):
		v7 = 14
	elif v6 == 4:
		v7 = 13
	elif v6 ==3:
		v7 = 12
	else:
		v7 = (v6==2) + 10

	str1.append(chr(ord(str2[v4]) - v7))


	v8 = v5%5
	if v5 == 5*((v5)//5):
		v9 = 14
	elif v8 == 4:
		v9 = 13
	elif v8 == 3:
		v9 = 12
	else:
		v9 = (v8==2) + 10

	str1.append(chr(ord(str2[v4+1]) - v9))

	v10 = (v5+1)%5
	if v5+1 == 5*((v5+1)//5):
		v11 = 14
	elif v10 == 4:
		v11 = 13
	elif v10 == 3:
		v11 = 12
	else:
		v11 = (v10 == 2) + 10

	str1.append(chr(ord(str2[v4+2]) - v11))

	v12 = (v5+2)%5
	if v5+2 == 5*((v5+2)//5):
		v13 = 14
	elif v12 == 4:
		v13 = 13
	elif v12 == 3:
		v13 = 12
	else:
		v13 = (v12 == 2) + 10
	str1.append(chr(ord(str2[v4+3]) - v13))

	v14 = (v5+3)%5
	if v14+3 == 5*((v5+3)//5):
		v15 = 14
	elif v14 == 4:
		v15 = 13
	elif v14 == 3:
		v15 = 12
	else:
		v15 = (v14==2) + 10

	str1.append(chr(ord(str2[v4+4]) - v15))

	v5 += 5
	v4 += 5

print(''.join(str1))
