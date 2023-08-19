from pwn import *

io = remote('62.173.140.174', 11000)

hashes = []
io.recvuntil(b'$ ')

print("Getting hashes...")
count = 5000
for i in range(count):
    io.sendline(b'request')
    io.recvuntil(b'$ ')
    if io.recv(4) == b'[-] ':
        continue
    hashes.append(io.recv(46).decode('ascii'))
    io.recvline()
io.close()
#print(f"Hashes we got: {hashes}")

print("Decoding hashes...")
list1 = []
flag = []
symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}!$@%^&*()"

for i in range(len(hashes)):
    hashes[i] = bytes.fromhex(hashes[i])

for x in range(23):
    for a in symbols:
        for i in range(len(hashes)):
            if hashes[i][int(x)] == ord(a):
                if a in list1:
                    list1.remove(a)
                break
            else:
                if a not in list1:
                    list1.append(a)
    flag += list1
print(''.join(flag))