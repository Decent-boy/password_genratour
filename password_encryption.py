"""this code is mine"""
import os
from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
# write_key()
def load_key():
    with open("key.key","rb") as file:
        key=file.read()
    return (key)
key=load_key()
master_psw=input("Type master password: ")
# key=load_key() + master_psw.encode()
fer=Fernet(key)
def add():
    name=input("Enter Account name: ")
    pwd=input("Enter Your password: ")
    # ecrypting from here
    encrypt_pwd=fer.encrypt(pwd.encode())
    with open("password.txt","a") as f:
        f.write(f"{name} | {encrypt_pwd.decode()}\n")
def view():
    try:
        with open("password.txt","r") as f:
            for line in f.readlines():
                data=line.rstrip()
                user,pssw=data.split("|")
                # decrypting password
                decrypt_pssw=fer.decrypt(pssw.strip().encode().decode())
                print(f"user: {user.strip()}|password {decrypt_pssw}")
    except FileNotFoundError:
        print("file is not occourde")
    except Exception as e:
        print(f"error {e}") 

           
def dele():
    print("removed successfully")
    os.remove("password.txt")
def qu():
    print("Done")
    quit()
while True:
    try:
        mode=input("Type (add) for Add, (v) for view, (Q) for Quite and (D) for delete\n Type here: ")
        if mode.lower().strip()=="q":
            qu()
        elif mode.lower().strip()=="d":
            dele()
        elif mode.lower().strip()=="add":
            add()
        elif mode.lower().strip()=="v":
            view()
        else:
            print("You are typing invalid words")
    except ValueError:
        print("It's a error")
    finally:
        print("best of luck")

""""this is code of chat gpt"""

# import os  
# from cryptography.fernet import Fernet  

# def write_key():  
#     """ Generate and save a key for encryption. """  
#     key = Fernet.generate_key()  
#     with open("key.key", "wb") as key_file:  
#         key_file.write(key)  

# # Uncomment the following line if the key needs to be generated only once.  
# # write_key()  

# def load_key():  
#     """ Load the encryption key from a file. """  
#     with open("key.key", "rb") as file:  
#         key = file.read()  
#     return key  

# # Load the encryption key  
# key = load_key()  
# master_psw = input("Type master password: ")  # Master password not currently used in key management  
# fer = Fernet(key)  

# def add():  
#     """ Add a new account and encrypt the password. """  
#     name = input("Enter Account name: ")  
#     pwd = input("Enter Your password: ")  
#     # Encrypting the password  
#     encrypt_pwd = fer.encrypt(pwd.encode())  # Make sure to pass bytes for encryption  
#     with open("password.txt", "a") as f:  
#         f.write(f"{name} | {encrypt_pwd.decode()}\n")  # Store the encrypted password as string  

# def view():  
#     """ View stored accounts and their passwords. """  
#     try:  
#         with open("password.txt", "r") as f:  
#             for line in f.readlines():  
#                 data = line.rstrip()  
#                 user, pssw = data.split("|")  
#                 # Decrypting password  
#                 decrypt_pssw = fer.decrypt(pssw.strip().encode())  # Pass bytes for decryption  
#                 print(f"user: {user.strip()} | password: {decrypt_pssw.decode()}")  # Decode the decrypted byte result  
#     except FileNotFoundError:  
#         print("File not found.")  
#     except Exception as e:  
#         print(f"Error: {e}")  

# def dele():  
#     """ Delete the password file. """  
#     if os.path.exists("password.txt"):  
#         os.remove("password.txt")  
#         print("Password file removed successfully.")  
#     else:  
#         print("Password file does not exist.")  

# def qu():  
#     """ Exit the program. """  
#     print("Done")  
#     quit()  

# # Main program loop  
# while True:  
#     try:  
#         mode = input("Type (add) for Add, (v) for view, (Q) for Quit and (D) for delete\nType here: ")  
#         if mode.lower().strip() == "q":  
#             qu()  
#         elif mode.lower().strip() == "d":  
#             dele()  
#         elif mode.lower().strip() == "add":  
#             add()  
#         elif mode.lower().strip() == "v":  
#             view()  
#         else:  
#             print("You are typing invalid words.")  
#     except ValueError:  
#         print("It's an error.")  
#     finally:  
#         print("Best of luck!")