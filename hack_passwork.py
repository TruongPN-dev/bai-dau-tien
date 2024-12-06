import os
from random import randint
import time
from threading import Thread

password = input("Nhập mật khẩu: ")
key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
       'u', 'v', 'w', 'x', 'y', 'z']

pwg = ''
cout = 0
found_password = False  # Biến cờ để kiểm soát thread

def symbol():
    key = ["\\", "|", "/", "-"]
    while not found_password:  # Kiểm tra biến cờ trước mỗi lần lặp
        for i in key:
            print("Loading...." + i, end="\r")
            time.sleep(0.03)

def guess_password():
    global found_password  # Sử dụng biến toàn cục
    global pwg
    global cout
    while not found_password:
        pwg = ''
        for i in range(len(password)):
            guessPass = key[randint(0, len(key) - 1)]
            pwg = str(guessPass) + str(pwg)
        cout += 1
        if pwg == password:
            found_password = True

# Khởi tạo và bắt đầu thread
thread1 = Thread(target=symbol)
thread1.start()

# Bắt đầu thread đoán mật khẩu
guess_thread = Thread(target=guess_password)
guess_thread.start()

# Chờ thread đoán mật khẩu kết thúc
guess_thread.join()

# Dừng thread hiển thị biểu tượng
found_password = True
thread1.join()

os.system('cls')
print(f'Mật khẩu là: {pwg}')
print(f"Số lần thử là: {cout}")
