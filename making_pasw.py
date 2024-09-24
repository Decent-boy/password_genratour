import random
import string
def genrate():
    name=input("enter your name for making password: ")
    if len(name)<=3:
        name=name[1:] + name[0]
        print(name)
    elif len(name)>=4 and len(name)<=30:
        alphabet=string.ascii_lowercase
        chracter=string.punctuation
        digits=string.digits
        random_alpha=random.choice(alphabet)
        random_digits=random.choice(digits)
        random_chra=random.choice(chracter)
        name=name[1:] + name[0]
        print(name + random_alpha +random_digits +random_chra)
    else:
        print("error")
# genrate()
while True:
    try:

        user_input=input("are you wanted to make a password\ntype(y) for Yes\ntype (Q) for quit\nType Here: ")
        if user_input.lower()=="y":
            genrate()
        elif user_input.lower().strip()=="q":
            quit()
        else:
            print("invalid statement")
    except ValueError:
        print("error")