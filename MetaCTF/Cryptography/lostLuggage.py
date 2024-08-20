import zipfile
import itertools

digits = "0123456789"
zf = zipfile.ZipFile("luggage.zip")
for combination in itertools.product(digits, repeat=4):
	password = ''.join(combination)
	try:
		zf.extractall(pwd=password.encode('utf-8'))
		print(f'password is {password}')

	except:
		continue
