This was a pretty simple problem. If we use binwalk on the disc image using

		gunzip -d disk.flag.img.gz && binwalk -e disk.flag.img

We will get an extracted directory and this output,

		DECIMAL       HEXADECIMAL     DESCRIPTION
		--------------------------------------------------------------------------------
		1048576       0x100000        Linux EXT filesystem, blocks count: 102400, image size: 104857600, rev 1.0, ext4 filesystem data, UUID=496a2407-fed5-477e-bb77-09b9cb4acb4a
		210763776     0xC900000       Linux EXT filesystem, blocks count: 203776, image size: 208666624, rev 1.0, ext4 filesystem data, UUID=7b688671-b1b5-4e64-830d-36ebc2d4c2d4


It's describing two filesystems that we will need to analyse. So, going into the `_disk.img.flag.extracted` directory, we see the following files.

		100000.ext  C900000.ext  ext-root  ext-root-0


Here, you need to look around a little bit and see what is going on. But it's rather simple. If you move into `ext-root-0` you will see a linux filesystem analogous to what we are used to. Naturally the most interesting directory is the `root` so once we move into root we will see the encryped flag!

Now keeing in mind that the challenge's name is `operation orchid` which is often called `operation think-outside-the-box`, we should check for hidden files. And sure enough we find the command that was used to encrypt this flag,

		openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567


Thus, we must decrypt the flag using,

		openssl aes-256-cbc -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567


And we're done.