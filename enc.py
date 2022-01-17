from cryptography.fernet import Fernet
import os


def create_enc_key1(website):
    key = Fernet.generate_key()

    with open(f"{website}.key", "wb") as filekey:
        filekey.write(key)


def encrypt_settings():
    create_enc_key1("settings")
    with open("settings.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("settings.json", "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("settings.json", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_settings():
    with open("settings.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("settings.json", 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("settings.json", 'wb') as dec_file:
        dec_file.write(decrypted)

    os.remove("settings.key")


def create_enc_key():
    key = Fernet.generate_key()

    with open("data.key", "wb") as filekey:
        filekey.write(key)


def encrypt():
    create_enc_key()
    with open("data.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("data.db", "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("data.db", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt():
    with open("data.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("data.db", 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("data.db", 'wb') as dec_file:
        dec_file.write(decrypted)

    os.remove("data.key")
