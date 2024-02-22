#!/usr/bin/env python3

string1 = 'affsemrgrdbimozmirbadyggp'
actual1 = 'immunoelectrophoretically'
mapping = {}
for i, letter in enumerate(string1):
	mapping[letter] = actual1[i]
  
string2 = 'rgrdbimredrozygmkiyozadyg'
actual2 = 'electroencephalographical'
new_mapping = {}
for k, letter2 in enumerate(string2):
	new_mapping[letter2] = actual2[k]

mapping.update(new_mapping)
print(mapping)
print(len(mapping))

string3 = 'yebavaurubyngauzfrebyiaye'
actual3 = 'antidisestablishmentarian'
new_new_mapping = {}
for t, letter3 in enumerate(string3):
	new_new_mapping[letter3] = actual3[t]

mapping.update(new_new_mapping)
print(mapping)
print(len(mapping))

flag2 = 'orizyou_bzr_vmk_lsforv_mwri_xyu_lsub_bairv'
alphabets = 'abcdefghijklmnopqrstuvwxyz'

def crack(flag):
	flag_d = ''
	for p in flag:
		if p in alphabets:
			try:
				flag_d += mapping.get(p)
			except Exception:
				flag_d += '*'
		else:
			flag_d += p
	print(flag_d)
crack(flag2)
