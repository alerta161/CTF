import socket
import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

BUFFER_SIZE = 10000
WAIT_INTERVAL = 0.5


def main():
    host = "62.173.140.174"
    port = 10006

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print("Connected to server")
            response = s.recv(1024).decode()
            print(response)
            s.send(b"start\n")
            response = s.recv(1024).decode()
            print(response)

            while True:
                time.sleep(WAIT_INTERVAL)
                buffer = s.recv(BUFFER_SIZE)
                qr_data = buffer.decode()
                print(qr_data)
                with open('qr.png', 'w') as file:
                    save_qr(buffer, 'qr.png')
                    decoded = decode_qr('qr.png')
                    s.send(decoded.encode() + b"\n")
        except Exception as e:
            print(f"Error: {e}")


def save_qr(buffer, file_path):
    qr_ascii = cut_qr(buffer)
    bitmap = get_bitmap(qr_ascii)
    img = create_img(bitmap)
    save_img(img, file_path)


def cut_qr(buffer):
    qr_str = buffer.decode()
    str_list = qr_str.split("\n")
    ascii_qr_strs = [s for s in str_list if "[" in s]
    return ascii_qr_strs


def get_bitmap(ascii_qr_strs):
    bitmap = []
    for line in ascii_qr_strs:
        pixels = line.split("  ")
        pixels = pixels[:-1]
        row = [True if "[42m" in pixel else False for pixel in pixels]
        bitmap.append(row)
    return bitmap


def create_img(bitmap):
    img = np.zeros((len(bitmap), len(bitmap[0]), 3), dtype=np.uint8)
    for y, row in enumerate(bitmap):
        for x, val in enumerate(row):
            if val:
                img[y, x] = [0, 0, 0]  # Black
            else:
                img[y, x] = [255, 255, 255]  # White
    return img


def save_img(img, file_path):
    img_pil = Image.fromarray(img)
    img_pil.save(file_path, "png")
    print("Image saved")


def decode_qr(file_path):
    img = cv2.imread(file_path)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode()
    return ""


if __name__ == "__main__":
    main()
