import subprocess
import zxing

target_ip = "62.173.140.174"
target_port = 10006


def communicate_with_server(command):
    try:
        nc_command = f"echo '{command}' | nc {target_ip} {target_port}"
        process = subprocess.Popen(nc_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode().strip()
    except Exception as e:
        print(f"Ошибка при выполнении команды nc: {e}")
        return None


def read_and_send_qr_codes():
    while True:

        qr_code = communicate_with_server("start")

        if qr_code:
            print(f"Прочитан QR-код: {qr_code}")

            decoded_result = zxing.BarCodeReader().decode(qr_code)

            if decoded_result:
                result = decoded_result.raw
                print(f"Расшифрованный результат: {result}")

                communicate_with_server(result)
            else:
                print("Не удалось расшифровать QR-код.")
        else:
            print("Не удалось получить QR-код от сервера.")


if __name__ == "__main__":
    read_and_send_qr_codes()
