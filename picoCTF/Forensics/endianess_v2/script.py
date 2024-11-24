# Regards - ChatGPT

import struct

def change_endianness(input_file, output_file, chunk_size):
    with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
        while chunk := infile.read(chunk_size):
            if len(chunk) == chunk_size:
                reversed_chunk = chunk[::-1]
                outfile.write(reversed_chunk)
            else:
                outfile.write(chunk)

input_file = r""
output_file = "output"
chunk_size = 4  # Change to 2 for 16-bit words, 8 for 64-bit words, etc.
change_endianness(input_file, output_file, chunk_size)
