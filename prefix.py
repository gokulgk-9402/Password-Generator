key = ''

with open("key.key", 'rb') as f:
    key = f.read()

data = ''
with open("prefix.txt", 'rb') as f:
    data = f.read()

from cryptography.fernet import Fernet

f = Fernet(key)

encrypted_data = f.encrypt(data)

with open("prefix.key", "wb") as f:
    f.write(encrypted_data)