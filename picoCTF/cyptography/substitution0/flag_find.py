#!/usr/bin/env python3

key = 'DECKFMYIQJRWTZPXGNABUSOLVH' # given key
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dictionary = {}
for i in range(0, 26):
	dictionary[key[i]] = alphabets[i]

message = 'xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}'
decoded = ''

for i in message:
	if i in alphabets:
		decoded += dictionary.get(i)
	else:
		decoded += f'{i}'
print(decoded)
