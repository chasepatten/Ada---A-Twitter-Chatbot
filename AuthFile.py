from cryptography.fernet import Fernet


def generate_key():
    # Generate a new key.
    key = Fernet.generate_key()
    print("-New key generated.")
    # Put the key string into a file named filekey
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
        print("-Filekey file, ready.")

        filekey.close()
        print("-Filekey Closed.")


def encrypt_file():
    # Opening the file containing the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        print("-Key read successfully.")
    # Place the key in an object
    fernet = Fernet(key)
    print("-Object key created.")

    # Open the original file to encrypt
    # Cant figure out how to pass list to this function so, you have to direct path the file for now
    with open('ada', 'rb') as file:
        original = file.read()
        print("-File read.")

    # Encrypt the file
    encrypted = fernet.encrypt(original)

    # Open the file in write mode
    with open('ada', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        print("-File encrypted.")

    filekey.close()
    print("-Encryption Key Closed.")
    encrypted_file.close()
    print("-Encrypted File Closed.")


def decrypt_file():
    # Opening the file containing the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        print("-Key read successfully.")
    # Place the key in an object
    fernet = Fernet(key)
    print("-Object key created.")

    # Opening the encrypted file to be decrypted
    with open('ada', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    # Decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # Opening the file in write mode and decrypting the file
    with open('ada', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        print("-File decrypted.")

    decrypted_file.close()
    print("-Decrypted file closed.")





