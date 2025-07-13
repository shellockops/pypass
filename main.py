import pypass

def main():
    password = "love2d"   #pypass.gen_password()
    #print(password)
    entropy = pypass.find_entropy(password)

    print("The entropy of your password is: ", entropy)
    occurency = pypass.check_db(password)

    if occurency:
        print(f"This password has been seen {occurency:,} times before in data breaches!\nChange it immediately!!!")
    else:
        print("This password wasn't found in any of the Pwned Passwords loaded into Have I Been Pwned.\nThat doesn't necessarily mean it's a good password, merely that it's not indexed on this site.")

main()