import pypass

def main():
    #password = pypass.gen_password()
    #print(password)
    entropy = pypass.find_entropy("1Bankruptcies2&%")
    print(entropy)
main()