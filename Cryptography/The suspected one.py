def long_to_bytes(n, byteorder='big'):
    if n == 0:
        return b'\x00'
    elif n < 0:
        raise ValueError("Only non-negative integers are supported")
    else:
        return n.to_bytes((n.bit_length() + 7) // 8, byteorder)


# Example usage:
n = 6446982264000635652948556502623658209996049063529575549
byte_representation = long_to_bytes(n)
print(byte_representation)
