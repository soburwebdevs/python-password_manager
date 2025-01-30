from cryptography.fernet import Fernet

def load_key():
    with open('key.key', 'rb') as file:
        return file.read()

key = load_key()  # Load key without concatenation
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.rstrip().split("|")
            decrypted_pwd = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_pwd)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Convert bytes to string

    with open('password.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")  # Fixed concatenation issue

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")



