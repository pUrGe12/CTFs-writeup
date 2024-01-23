import sys

a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

# arg133 = func1
# arg432 = val1
def func1(val1):
  if val1 == 'happychance':
    return True
  else:
    print('That password is incorrect')
    sys.exit(0)
    return False

# arg111 = func2
# arg444 = val2
def func2(val2):
  return func6(val2.decode(), 'rapscallion')

# arg232 = func3
def func3():
  return input('Please enter correct password for flag:')
# arg132 = func4

def func4():
  return open('flag.txt.enc', 'rb').read()

# arg112 = func5
def func5():
  print('Welcome back... your flag, user:')

# arg122 = func6
# arg432 = val1
# arg423 = val3
# arg433 = val4
# arg422 = val5
# arg442 = val6

def func6(val1, val3):
    val4 = val1
    i = 0
    while len(val4) < len(val1): # this part is pretty much the issue, why an empty string is returned. Run the actual code with the password 'happychance'
        val4 += val3[i]
        i = (i + 1) % len(val3)
    return "".join([chr(ord(val5) ^ ord(val6)) for (val5,val6) in zip(val1,val4)])

func1(func3()) # correct password is happychance
func5()

enc_flag = open('flag.txt.enc','rb').read()
val3 = func6(enc_flag.decode(), 'rapscallion')

print(val3)
sys.exit(0)
