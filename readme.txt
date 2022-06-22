This is a program to generate a random password with a specified prefix and a number of random characters, and store them in a file, encrypt it using a key. The passwords stored can be accessed by inputing the master password (which is also stored in an encrypted file) and the required password will be directly copied to the clipboard. You can either generate a password or input an existing password or update an existing password or replace an existing password with a new generated password or view any of the password you want to view.

The popular python library 'cryptography' is used to encrypt the file containing the passwords.

Steps to run the program:
1) First input the required password prefix, and the required master password in the files "prefix.txt" and "master.txt" respectively.
2) Run the code key_generator.py
3) Run the code prefix.py and master_pass.py to generate encrypted files containing the prefix and master password.
4) You can now delete the files prefix.txt and master.txt.
5) Now you can normally run the main.py file.
6) Be sure to not delete/modify the file key.key that is generated.
7) The encrypted file containing the master password -> master.key, prefix -> prefix.key, passwords -> passwords.key are important files.
8) Have fun using the password generator and never forget a password again.
9) For now there is no GUI for the program, I am planning to make one shortly.


Feel free to let me know your thoughts :D
