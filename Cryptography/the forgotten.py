cipher_text = b"+\x7ft1*iK\x1c[Io\x16\x1a\x00o\x1aYS\x03+\x10\x00B\t"
key = b"h00t"

decoded_text = bytearray(len(cipher_text))

for i in range(len(cipher_text)):
    decoded_text[i] = cipher_text[i] ^ key[i % len(key)]

print(decoded_text.decode('utf-8'))
