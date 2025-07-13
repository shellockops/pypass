import string
import secrets
from math import log2, floor
import hashlib
import requests

def gen_password():
    default_size = 20

    total = []
    total.append(string.ascii_lowercase)
    total.append(string.ascii_uppercase)
    total.append(string.punctuation)
    total.append(string.digits)

    password = ""

    count = 0
    for i in range(default_size + 1):
        password += secrets.choice(total[count])
        if count < 3:
            count += 1
        else:
            count = 0

    mix = list(password)
    secrets._sysrand.shuffle(mix)

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


def check_db(password):

    sha1_pass = hashlib.sha1(password.encode()).hexdigest()

    url = f"https://api.pwnedpasswords.com/range/{sha1_pass[:5]}"
    sha1_postfix = sha1_pass[5:].upper()

    response = requests.request("GET", url)
    pwned_list = response.text.split("\n")
    hash_dict = {}

    for pwned_pass in pwned_list:
        pwned_hash_times = pwned_pass.split(":")
        hash_dict[pwned_hash_times[0]] = pwned_hash_times[1]
    
    count = 0
    for key, value in hash_dict.items():
        if sha1_postfix in key:
            count += int(value)
    
    return count