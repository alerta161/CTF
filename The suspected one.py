binary_string = """01001001
00001000
01101111
11010011
01010101
11100100
10101101
00011010
10011011
00000100
00111101
00010111
11001111
10100101
00101100
01110001
00000000"""

# Split the binary string into 8-bit chunks
binary_values = binary_string.split()

# Convert each binary value to its decimal equivalent and then to a character
decoded_text = ''.join([chr(int(binary, 2)) for binary in binary_values])

print(decoded_text)
