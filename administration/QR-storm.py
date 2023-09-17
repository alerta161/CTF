import os
import time

import cv2
from pwn import *
from pyzbar.pyzbar import decode
from PIL import ImageGrab, Image  # Use Pillow for taking screenshots


# Function to read a QR code from an image file
def read_qr_code(filename):
    try:
        img = Image.open(filename)
        gray_image = img.convert('L')
        binary = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
        binary.save('temp.png', format='PNG')

        image = cv2.imread('temp.png')
        barcodes = decode(image)

        if barcodes:
            return barcodes[0].data.decode()
        else:
            return None

    except Exception as e:
        return None


context(arch='i386', os='linux')

ip = '62.173.140.174'
port = 10006

# Connect to the remote server with error handling
try:
    r = remote(ip, port)
except Exception as e:
    print("Error connecting to the server:", str(e))
    exit()

# Send the "start" command to the server
r.sendline(b'start')

# Loop to process QR codes
try:
    for i in range(0, 50):
        data = r.recvuntil(b'/50) ', timeout=5)  # Adjust the timeout as needed
        if not data:
            print("Connection closed unexpectedly.")
            break

        print(data.decode())

        time.sleep(1)

        # Take a screenshot using Pillow and save it
        screenshot = ImageGrab.grab()
        screenshot.save("qr.png")

        # Read the QR code from the screenshot
        qr_code_data = read_qr_code("qr.png")

        if qr_code_data:
            print("QR Code Data:", qr_code_data)
            r.sendline(qr_code_data.encode())
        else:
            print("No QR code detected in the screenshot.")
            r.sendline(b'')  # Send an empty line if no QR code is detected

except EOFError:
    print("Connection closed unexpectedly.")

# Close the connection
r.close()
