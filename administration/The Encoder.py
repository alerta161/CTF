import base64
import socket
import time


def main():
    host = "62.173.140.174"
    port = 10002

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to", host, "on port", port)

        s.sendall(b"start\n")

        while True:
            time.sleep(0.5)
            response = s.recv(10000)
            text = response.decode().strip().split()[-2]
            if text == "FLAG:":
                text = response.decode().strip().split()[-1]
            print("Received Text:", text)

            encoded_text = base64.b32encode(text.encode()).decode()
            print("Encoded Text:", encoded_text)

            s.sendall((encoded_text + "\n").encode())


if __name__ == "__main__":
    main()
