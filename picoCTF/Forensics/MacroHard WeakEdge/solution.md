Download the given pptm file. We can see that it contains 3 differnet directories. 

**A pptm file can house multiple directories and works like a zip file**

Go over to the downloads folder and click the extract button. Run the following commands to search for potential places the flag might be

1. `$grep -r flag`
2. `$grep -r pico`
3. `$grep -r hidden`

The first two will give no results but the 3rd gives a result.

use command `$ cd ppt/slideMasters`
search the files there to find a file named 'hidden'. use `$cat hidden` to view its contents 'Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q'

use cyberchef to decode this string from base64 to obtain the flag. (it's not immediately obvious that this is a base64 encoding but the goal with cyberchef is to use multiple algorithms until the decrypted string is found).

`flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}`
