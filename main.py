import string
import random

def main():


    size = 20

    total = []
    total.append(string.ascii_lowercase)
    total.append(string.ascii_uppercase)
    total.append(string.punctuation)
    total.append(string.digits)

    password = ""

    count = 0
    for i in range(21):
        password += random.choice(total[count])
        if count < 3:
            count += 1
        else:
            count = 0

    mix = list(password)
    random.shuffle(mix)

    print("".join(mix))
main()