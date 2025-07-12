import string
import random
from math import log2, floor

def gen_password():
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

    return "".join(mix)

def find_entropy(password):
    
    size = len(password)
    keep_pass_track = {"lower": False, "upper": False, "digit": False, "punc": False}

    for char in password:
        if char.islower():
            keep_pass_track["lower"] = True
        elif char.isupper():
            keep_pass_track["upper"] = True
        elif char.isdigit():
            keep_pass_track["digit"] = True
        elif char in string.punctuation:
            keep_pass_track["punc"] = True
    
    char_range = 0

    if keep_pass_track["lower"] == True:
        char_range += 26
    if keep_pass_track["upper"] == True:
        char_range += 26
    if keep_pass_track["digit"] == True:
        char_range += 10
    if keep_pass_track["punc"] == True:
        char_range += 32
    
    entropy = (size * log2(char_range))
    entropy = floor(entropy * 10) / 10
    
    return entropy
