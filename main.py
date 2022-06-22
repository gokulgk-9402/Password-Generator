import random
import json
import os
import time
from cryptography.fernet import Fernet
import clipboard
import getpass

key = ''

with open("key.key", 'rb') as file:
    key = file.read()

f = Fernet(key)

masterp = ''
with open("master.key", 'rb') as file:
    masterp = file.read()

mp = f.decrypt(masterp)

mp = mp.decode()

def new_pass(site, username, password):
    pass_dict = {}

    if os.path.exists("passwords.key"):
        data = ''
        with open("passwords.key", 'rb') as file:
            data = file.read()

        decrypted = f.decrypt(data)

        with open("passwords.json", "wb") as file:
            file.write(decrypted)

        with open("passwords.json", "r") as file:
            pass_dict = json.load(file)

        os.remove("passwords.json")

    new_pass = {'username': username, 'password': password}

    if site in pass_dict.keys():
        found = 0
        for ele in pass_dict[site]:
            if ele['username'] == username:
                ele['password'] = password
                print("Updated records successfully")
                found = 1
                break
        if found == 0:
            pass_dict[site].append(new_pass)
    else:
        lst = []
        lst.append(new_pass)
        pass_dict[site] = lst

    with open("passwords.json", "w") as file:
        json.dump(pass_dict, file)

    data = ''
    with open("passwords.json", 'rb') as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open("passwords.key", "wb") as file:
        file.write(encrypted_data)

    os.remove("passwords.json")

def get_pass():
    pass_dict = {}

    if os.path.exists("passwords.key"):
        data = ''
        with open("passwords.key", 'rb') as file:
            data = file.read()

        decrypted = f.decrypt(data)

        with open("passwords.json", "wb") as file:
            file.write(decrypted)

        with open("passwords.json", "r") as file:
            pass_dict = json.load(file)

        os.remove("passwords.json")

        print("List of available sites: ")
        sites = pass_dict.keys()
        for site in sites:
            print(site)

        site = input("Enter the site: ")

        if site not in pass_dict.keys():
            return 0, site, None

        else:
            print("List of available usernames: ")
            for ele in pass_dict[site]:
                print(ele['username'])
            uname = input("Enter the username: ")
            found = 0
            for ele in pass_dict[site]:
                if ele['username'] == uname:
                    found = 1
                    return 1, site, uname, ele['password']
            if found == 0:
                return 0, site, uname, None

    else:
        return 0, None, None, None

def random_pass(site, length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*(),.?0123456789'

    password = pass_prefix + site 

    for i in range(length):
        password += random.choice(chars)

    return password


print("Welcome to this password manger")

master_pass = getpass.getpass("Enter master password: ")

if master_pass != mp:
    print("Wrong master password entered!")
    quit()

pass_prefix = ''
with open("prefix.key", 'rb') as file:
    pass_prefix = file.read()

pass_prefix = f.decrypt(pass_prefix)

pass_prefix = pass_prefix.decode()

cont = True

while cont == True:

    choice = int(input("What do you want to do?\n1 - Generate new password\n2 - Input an existing password\n3 - Upadate an existing password\n4 - View & copy existing passwords\n5 - Quit\n"))

    if choice == 1:

        site = input("Enter the site for which you need password: ")

        username = input("Enter the username/email/number you are creating the password for: ")

        length = int(input("Enter length of random pass: "))

        password = random_pass(site, length)

        clipboard.copy(password)
        print("Password generated and copied to clipboard!")

        new_pass(site, username, password)
        print("Successfully updated the passwords record!")

    elif choice == 2:
        site = input("Enter site for which you want to input password: ")
        username = input('Enter username for which you want to input password: ')
        password = input('Enter password that you want to input: ')

        new_pass(site, username, password)
        print("Successfully updated the passwords record!")

    elif choice == 3:
        result,site, username, pwd = get_pass()

        if result == 0:
            print("No records found!")

        else:
            ch2 = int(input("Do you want to\n1 - Generate new password\n2 - Input new password\nEnter choice: "))
            if ch2 == 1:
                length = int(input("Enter length of random pass: "))
                new_password = random_pass(site, length)

            elif ch2 == 2:
                new_password = input("Enter new password: ")

            new_pass(site, username, new_password)
            clipboard.copy(new_password)
            print("New password copied to clipboard!")

    elif choice == 4:
        result, site, username, password = get_pass()

        if result == 0:
            print("No records found!")

        else:
            clipboard.copy(password)
            print("Password copied to clipboard!")

    elif choice == 5:
        break

    cont_txt = input("Do you want to continue?(y/n) ")

    if cont_txt.lower() == "n":
        cont = False

print("Thank you for using this password manager")