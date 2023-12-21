import stepic
from PIL import Image
from cryptography.fernet import Fernet



key = input("Key: ")
dec = Fernet(key)

file = input("Photo: ")

img = Image.open(file)
decoded = stepic.decode(img)
text_dec = dec.decrypt(decoded.encode())

print("Data is: "+ text_dec.decode())




